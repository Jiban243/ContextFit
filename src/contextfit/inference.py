from .validation import validate_record
import time
import torch

model = None
tokenizer = None

def configure(loaded_model, loaded_tokenizer):
    global model, tokenizer
    model = loaded_model
    tokenizer = loaded_tokenizer

def measure_generation(inputs, max_new_tokens=80):
    torch.cuda.synchronize()
    baseline = torch.cuda.memory_allocated()
    torch.cuda.reset_peak_memory_stats()

    start = time.perf_counter()

    with torch.inference_mode():
        output = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )

    torch.cuda.synchronize()
    elapsed = time.perf_counter() - start
    peak = torch.cuda.max_memory_allocated()

    input_count = inputs["input_ids"].shape[1]
    generated = output[0, input_count:]
    output_count = generated.numel()

    result = {
        "input_tokens": input_count,
        "output_tokens": output_count,
        "generation_seconds": elapsed,
        "output_tokens_per_second": output_count / elapsed,
        "baseline_allocated_gib": baseline / (1024**3),
        "peak_allocated_gib": peak / (1024**3),
        "extra_peak_allocated_mib": (peak - baseline) / (1024**2),
        "answer": tokenizer.decode(generated, skip_special_tokens=True),
    }

    return result

def prepare_inputs(question, context):
    if model is None or tokenizer is None:
        raise RuntimeError("Call configure(model, tokenizer) first.")

    messages = [
        {
            "role": "system",
            "content": (
                "Answer using only the supplied context. "
                "Cite the supporting document IDs, such as [doc1]. "
                "If the answer is missing, say you do not know. "
                "Keep the answer brief."
            ),
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}",
        },
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    encoded = tokenizer(
        prompt,
        return_tensors="pt",
        add_special_tokens=False,
        truncation=False,
    )

    input_tokens = encoded["input_ids"].shape[1]
    model_limit = getattr(model.config, "max_position_embeddings", 4096)
    total_limit = min(4096, model_limit)
    reserved_output_tokens = 80

    if input_tokens + reserved_output_tokens > total_limit:
        raise ValueError(
            f"Prompt has {input_tokens} tokens; "
            f"maximum input is {total_limit - reserved_output_tokens} "
            f"with {reserved_output_tokens} tokens reserved for output."
        )

    return encoded.to(next(model.parameters()).device)


def run_record(record):
    validate_record(record)
    prepared = prepare_inputs(
        question=record["question"],
        context=record["context"],
    )

    result = measure_generation(prepared)

    result.update({
        "question_id": record["question_id"],
        "policy": record["policy"],
        "source_ids": record["source_ids"],
    })

    return result
