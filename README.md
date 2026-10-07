# ContextFit

Evaluating how retrieved-context selection affects answer quality,
generation latency, and GPU memory for a RAG assistant on a single
NVIDIA T4.

## Problem Statement

A self-hosted RAG assistant has limited GPU resources. Sending unnecessary
retrieved context may increase processing time, while removing necessary
evidence may reduce answer quality.

ContextFit investigates this trade-off by comparing context-selection
policies under the same model, hardware, questions, and generation settings.

## Current Status

Jiban's initial GPU inference and benchmarking implementation is complete.
Ayush's retrieval and quality-evaluation work is the next phase.
Full RAG integration and final evaluation are pending.

This is an inference-systems experiment. It does not implement custom
CUDA kernels or claim production readiness.

## Team Contributions

### Jiban — GPU Inference and Performance Evaluation

Completed:

- Verified NVIDIA T4 execution in Google Colab.
- Loaded Qwen/Qwen2.5-1.5B-Instruct in FP16.
- Implemented evidence-based answer generation with citation instructions.
- Added request validation and source-marker checks.
- Enforced a 4,096-token total experiment limit, reserving 80 output tokens.
- Measured generation latency, token counts, and PyTorch allocated GPU memory.
- Implemented sequential benchmark execution with repeated measurements.
- Added per-attempt JSONL logging and skipping of completed jobs.
- Recorded environment details and experiment configuration.
- Packaged inference, benchmarking, and validation into Python modules.
- Ran a synthetic context-length experiment.

Remaining responsibilities:

- Integrate Ayush's prepared inference records.
- Run final GPU comparisons across context-selection policies.
- Analyze performance results and investigate failures.
- Contribute reproducibility instructions and the final demonstration.

### Ayush — Retrieval, Context Selection, and Quality Evaluation

Planned responsibilities:

- Select and prepare a public document collection.
- Implement document chunking and retrieval.
- Implement three context-selection configurations:
  1. Larger fixed top-k.
  2. Smaller fixed top-k.
  3. Token-budget selection.
- Prepare development and held-out evaluation questions.
- Record expected answers and supporting evidence separately from model inputs.
- Include direct, multi-passage, and unanswerable questions.
- Evaluate answer correctness, citation support, and unanswerable handling.
- Analyze cases where context reduction removes necessary evidence.

### Joint Responsibilities

- Agree on the dataset, prompt, and experimental settings.
- Review a shared subset of answer-quality assessments.
- Interpret performance and quality trade-offs.
- Complete documentation, limitations, and the demo.

## Current Model and Hardware

- Model: Qwen/Qwen2.5-1.5B-Instruct
- Precision: FP16
- Attention implementation: SDPA
- GPU: NVIDIA Tesla T4 in Google Colab
- Observed available GPU capacity: 14.56 GiB
- Maximum generated tokens: 80
- Experiment total-token limit: 4,096
- Maximum fully formatted input: 4,016 tokens
- Generation: greedy decoding (`do_sample=False`)

The 4,096-token limit is a project setting, not the model's advertised
maximum context length.

## Preliminary Synthetic Experiment

One question was asked with fixed supporting evidence and increasing
amounts of repetitive irrelevant text. Each input had two warm-up runs
and five timed repetitions.

| Context | Input tokens | Output tokens | Median generation time | Peak allocated memory | Correct fact | Citation present |
|---|---:|---:|---:|---:|---|---|
| Short | 80 | 17 | 0.662 s | 2.891 GiB | Yes | Yes |
| Medium | 865 | 20 | 0.950 s | 3.018 GiB | Yes | Yes |
| Long | 2,685 | 16 | 1.762 s | 3.809 GiB | Yes | No |

All three configurations answered the refund-window question correctly.
The long-context answer omitted the requested citation.

These are preliminary observations from one synthetic question.
They do not establish general RAG quality or real-world cost savings.
Raw experiment files are saved separately in Google Drive and are not
yet included in this repository.

## Measurement Scope and Limitations

- Timing covers `model.generate` after inputs are already on the GPU.
- It excludes retrieval, tokenization, model loading, and text decoding.
- GPU synchronization is used around the timed generation.
- Output token counts are recorded because response lengths can differ.
- Memory metrics measure PyTorch tensor allocations, not total GPU usage.
- Output tokens per second includes prompt processing; it is not decode-only speed.
- Requests execute sequentially; concurrent serving has not been evaluated.
- Time to first token is not yet measured.
- Citation formatting checks do not verify factual support.
- Resume skipping requires matching job inputs and configuration.
- Recovery from partially written JSONL lines is not yet implemented.

## Integration Contract

Ayush's retrieval pipeline will provide records in this format:

```json
{
  "question_id": "q001",
  "policy": "fixed_top_k",
  "question": "Within how many days can a customer request a refund?",
  "context": "[doc1] Customers can request a refund within 14 days.",
  "source_ids": ["doc1"]
}

