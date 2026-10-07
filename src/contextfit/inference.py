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

    return tokenizer(
        prompt,
        return_tensors="pt",
        add_special_tokens=False,
    ).to("cuda")

def run_record(record):
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
