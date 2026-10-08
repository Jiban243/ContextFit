from .validation import validate_record

SYSTEM_PROMPT = (
    "Answer using only the supplied context. "
    "Cite the supporting document IDs, such as [doc1]. "
    "If the answer is missing, say you do not know. "
    "Keep the answer brief."
)

MAX_INPUT_TOKENS = 4016
POLICIES = ("top_k_8", "top_k_2", "budget_900")


def count_tokens(tokenizer, text):
    return len(tokenizer.encode(text, add_special_tokens=False))


def format_context(chunks):
    return "\n\n".join(
        f"[{chunk['chunk_id']}] {chunk['text']}"
        for chunk in chunks
    )


def count_prompt_tokens(tokenizer, question, context):
    # Must match Jiban's inference prompt exactly.
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
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
    return count_tokens(tokenizer, prompt)


def build_request(question_id, question, candidates, policy, tokenizer):
    if policy not in POLICIES:
        raise ValueError(f"Unknown policy: {policy}")

    candidate_ids = [c["chunk_id"] for c in candidates]
    if len(candidate_ids) != len(set(candidate_ids)):
        raise ValueError("Duplicate candidate chunk IDs.")

    if policy == "top_k_8":
        selected = candidates[:8]

    elif policy == "top_k_2":
        selected = candidates[:2]

    else:
        selected = []

        for chunk in candidates:
            trial = selected + [chunk]
            context = format_context(trial)

            if (
                count_tokens(tokenizer, context) <= 900
                and count_prompt_tokens(
                    tokenizer, question, context
                ) <= MAX_INPUT_TOKENS
            ):
                selected = trial

    context = format_context(selected)
    prompt_tokens = count_prompt_tokens(
        tokenizer, question, context
    )

    if prompt_tokens > MAX_INPUT_TOKENS:
        raise ValueError(
            f"{policy}: formatted prompt has {prompt_tokens} tokens; "
            f"limit is {MAX_INPUT_TOKENS}. No truncation applied."
        )

    record = {
        "question_id": question_id,
        "policy": policy,
        "question": question,
        "context": context,
        "source_ids": [c["chunk_id"] for c in selected],
    }
    validate_record(record)

    diagnostics = {
        "question_id": question_id,
        "policy": policy,
        "candidate_count": len(candidates),
        "selected_count": len(selected),
        "context_tokens": count_tokens(tokenizer, context),
        "prompt_tokens": prompt_tokens,
        "selected_ids": record["source_ids"],
    }

    return record, diagnostics