# ContextFit

Evaluating how retrieved-context selection affects answer quality, generation latency, and GPU memory for a RAG assistant on a single NVIDIA T4.

## Problem Statement

A self-hosted RAG assistant has limited GPU resources. Sending unnecessary retrieved context may increase processing time, while removing necessary evidence may reduce answer quality.

ContextFit compares context-selection policies under the same model, hardware, questions, and generation settings. The goal is to measure resource savings alongside evidence retention and answer quality, rather than assume that shorter prompts are always better.

This is an application-level GPU inference experiment. It does not implement custom CUDA kernels or claim production readiness.

## Current Status

- Document preparation, chunking, BM25 retrieval, and three context-selection policies are implemented.
- The evaluation dataset contains six development questions and 24 test questions.
- The Colab T4 development benchmark completed 54 measured generations; the test benchmark completed 216.
- Raw test results, proposed answer grades, grading rules, and a findings report are included.
- Semantic grades are **assistant-proposed and pending human review**. Gold annotation review is also pending. They must not be presented as independently validated accuracy.

See [the results report](reports/RESULTS.md), [grading rubric](reports/EVALUATION_RUBRIC.md), and [answer review](reports/TEST_ANSWER_REVIEW.md).

## Team Contributions

### Jiban — GPU Inference and Benchmark Infrastructure

Completed:

- Verified NVIDIA T4 execution in Google Colab and loaded Qwen/Qwen2.5-1.5B-Instruct in FP16.
- Implemented context-based generation with citation and abstention instructions.
- Added request validation and source-marker checks.
- Enforced a 4,096-token total experiment limit, reserving 80 tokens for output.
- Measured generation latency, input/output token counts, and PyTorch allocated GPU memory.
- Implemented repeated, sequential benchmark execution with per-attempt JSONL logging and skipping of completed jobs.
- Packaged inference, benchmarking, and validation into Python modules.
- Recorded the initial synthetic context-length experiment.

### Ayush — Retrieval, Context Policies, and Integrated Evaluation

Completed:

- Prepared snapshots of three public Python documentation pages.
- Built 50 tokenizer-based chunks and deterministic BM25 retrieval.
- Implemented `top_k_8`, `top_k_2`, and `budget_900` context selection.
- Prepared development/test questions, expected answers, and alternative sufficient evidence sets, with assistant assistance.
- Kept expected answers and gold evidence separate from model inputs.
- Exported 18 development requests and 72 test requests with diagnostics and file hashes.
- Integrated the exported requests with Jiban's inference modules and verified prompt-token counts across Windows and Colab.
- Ran the development and test benchmarks on a Colab T4 and saved raw results.
- Added an assistant-assisted grading workflow, reproducible grade summaries, and failure analysis. Semantic review is not yet human-validated.

### Remaining Joint Work

- Review gold annotations and proposed answer grades, including borderline cases.
- Validate the final interpretation and prepare the demonstration.
- Preserve this baseline when conducting any future improvement experiments.

Jiban's inference and measurement infrastructure and Ayush's retrieval and evaluation pipeline are both necessary to compare the policies. Running the integrated benchmark does not replace ownership of the underlying modules.

## Dataset and Policies

The corpus consists of snapshots of the Python 3.13 tutorial pages on virtual environments, modules, and errors/exceptions. It contains 50 chunks with at most 300 tokens per chunk under the project tokenizer.

BM25 uses identical query/document tokenization, `k1=1.5`, and `b=0.75`. Each question retrieves up to ten positive-scoring candidates. Policies use the same ranked candidates.

| Policy | Selection rule |
|---|---|
| `top_k_8` | First eight candidates, or fewer if fewer are available |
| `top_k_2` | First two candidates, or fewer if fewer are available |
| `budget_900` | Greedily include whole chunks in rank order when the resulting context fits 900 tokens and the full prompt fits 4,016 tokens; skip chunks that do not fit |

The 900-token budget includes source markers but excludes the system instructions and question. Full prompts can therefore exceed 900 tokens.

The test set contains 15 single-chunk-answerable questions, three questions requiring combined evidence, and six questions unanswerable from the corpus. Development and test use the same document collection and share concepts; this is not a cross-domain generalization test.

## Model and Hardware

- Model: `Qwen/Qwen2.5-1.5B-Instruct`
- Precision: FP16; attention: SDPA
- GPU: NVIDIA Tesla T4 in Google Colab; observed capacity approximately 14.56 GiB
- Maximum generated tokens: 80; greedy decoding (`do_sample=False`)
- Experiment total-token limit: 4,096; maximum fully formatted input: 4,016
- Logged test environment: Python 3.13.15, PyTorch 2.11.0+cu130, Transformers 5.18.0, CUDA 13.0

The 4,096-token limit is a project setting, not the model's advertised maximum context length. The saved model revision is null, so the results do not identify a pinned model snapshot.

## Test Benchmark Results

Each of the 24 test questions was run under three policies with three sequential repetitions: **216 successful generations**. Warm-up was excluded. The runner shuffled jobs using seed 42. Generated text was identical across repetitions for every question-policy pair.

| Policy | Median input tokens | Median output tokens | Median generation time | Maximum peak allocated memory | Generations reaching 80 tokens |
|---|---:|---:|---:|---:|---:|
| `top_k_8` | 2,235.0 | 36.0 | 2.335 s | 3.651 GiB | 9/72 |
| `top_k_2` | 627.5 | 43.5 | 1.691 s | 2.974 GiB | 6/72 |
| `budget_900` | 910.5 | 51.0 | 2.147 s | 3.044 GiB | 9/72 |

These timing medians pool the 72 measured generations for each policy. Compared with `top_k_8`, the observed median time was 27.6% lower for `top_k_2` and 8.1% lower for `budget_900`. Output lengths differ, so this does not isolate the effect of input length or demonstrate a universal speedup.

### Proposed Quality Assessment — Human Review Pending

Quality is counted once per distinct question-policy answer. Timing repetitions are not independent quality samples.

| Policy | Full annotated evidence present | Fully correct | Partially correct | Incorrect | Abstention on unanswerable questions |
|---|---:|---:|---:|---:|---:|
| `top_k_8` | 18/18 | 7/18 | 6/18 | 5/18 | 4/6 |
| `top_k_2` | 16/18 | 6/18 | 4/18 | 8/18 | 3/6 |
| `budget_900` | 17/18 | 7/18 | 3/18 | 8/18 | 4/6 |

Correctness and abstention values are assistant-proposed semantic judgments. Both 4/6 abstention counts include a borderline decision documented in the rubric. Full-evidence counts mechanically check the annotated sufficient evidence sets; they depend on annotation quality. None of the 72 distinct test answers contained a source citation.

Key findings:

- Smaller contexts reduced observed generation time and peak allocated memory, but sometimes omitted necessary evidence.
- Having the annotated evidence did not guarantee a correct answer. All policies mishandled some exception and compiled-module questions.
- The fixed 80-token allowance cut off several answers before they completed the requested steps.
- The model sometimes treated historical documentation examples as current facts and frequently ignored citation instructions.

The project demonstrates a reproducible comparison and diagnosis, not a production-ready policy or proven monetary savings.

## Preliminary Synthetic Experiment

Before the integrated RAG benchmark, one refund-window question was tested with fixed supporting evidence and increasing repetitive irrelevant text. Each input had two warm-up runs and five timed repetitions.

| Context | Input tokens | Output tokens | Median generation time | Peak allocated memory | Correct fact | Citation present |
|---|---:|---:|---:|---:|---|---|
| Short | 80 | 17 | 0.662 s | 2.891 GiB | Yes | Yes |
| Medium | 865 | 20 | 0.950 s | 3.018 GiB | Yes | Yes |
| Long | 2,685 | 16 | 1.762 s | 3.809 GiB | Yes | No |

These observations concern one synthetic question, not general RAG quality. Synthetic raw files were saved separately in Google Drive; the committed raw test results below belong to the integrated Python-documentation benchmark.

## Run Locally

Local corpus preparation, retrieval, and evaluation summaries do not require a GPU. GPU generation runs in Colab.

From the project root on Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-retrieval.txt
```

On macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-retrieval.txt
```

With the committed dataset, run:

```bash
python scripts/check_evaluation.py
python scripts/export_requests.py
python scripts/summarize_evaluation.py
```

Exporting creates a new timestamped folder under `data/requests/`. The summary reads the committed proposed grades; it does not perform automatic semantic judging or GPU inference. Do not regenerate or replace the annotated gold dataset merely to reproduce a summary.

For a deliberate corpus rebuild, the preparation scripts are `scripts/prepare_documents.py` and `scripts/build_chunks.py`. Changing snapshots, tokenizer behavior, or chunks requires rechecking annotations and regenerating dependent exports. Use the committed snapshots and export artifacts when tracing the reported experiment.

## Run GPU Inference in Colab

Use `notebooks/ContextFit_02_RAG_Evaluation.ipynb` with a T4 runtime. The notebook mounts Google Drive at `/content/contextfit_drive` and uses:

- Source modules: `MyDrive/ContextFit/evaluation_src/contextfit/`
- Exported requests: `MyDrive/ContextFit/requests/<export_folder>/`
- Results: `MyDrive/ContextFit/results/<run_folder>/`

Upload `inference.py`, `benchmark.py`, `validation.py`, request files, diagnostics, and the export manifest as described in the notebook. Point its export path at the intended export, verify file hashes and token counts, load the model, warm up, and run the sequential benchmark. A fresh runtime requires rerunning setup and model loading; it does not inherit local notebook variables.

Resume skipping requires the same output file, request contents, and configuration. The notebook preserves a run directory when rerun in the same live session; after a runtime reset, explicitly select the existing directory to resume instead of starting a new run. Recovery from a partially written JSONL line is not implemented.

The inference module's prompt and the exporter's token-counting prompt must stay aligned. Changes to output allowance require consistent input reservation and configuration updates. Do not combine runs with different settings into one policy comparison.

## Evaluation and Artifacts

| Location | Purpose |
|---|---|
| `src/contextfit/inference.py` | Prompt preparation, CUDA generation, and measurement |
| `src/contextfit/benchmark.py` | Repeated execution, logging, and resume skipping |
| `src/contextfit/validation.py` | Request and source-marker validation |
| `src/contextfit/retrieval.py` | BM25 ranking |
| `src/contextfit/context_policies.py` | Context selection and full-prompt token checks |
| `data/raw/` | Document snapshots and metadata |
| `data/processed/` | Processed documents, chunks, and chunk manifest |
| `data/evaluation/` | Gold records, proposed grades, and grading manifest |
| `data/requests/` | Exported requests, diagnostics, and hashes |
| `results/contextfit_test_results.jsonl` | Raw test requests, generated answers, timings, and configuration |
| `reports/RESULTS.md` | Resource measurements, proposed quality findings, and limitations |
| `reports/TEST_ANSWER_REVIEW.md` | Per-answer evidence and proposed grading reasons |
| `reports/EVALUATION_RUBRIC.md` | Grading definitions and human-review instructions |

To produce a human-labelled summary only after actual review:

```bash
python scripts/summarize_evaluation.py --human
```

The command checks that review fields are populated and valid; it cannot verify that semantic judgments are correct. Never copy example scores across records. Keep proposed labels for audit, and record the actual reviewer and reasoning in human fields. Gold annotation review is separate from reviewing generated answers.

File hashes identify the original bytes. Git line-ending conversion on Windows can change byte hashes without changing parsed JSON; preserve original export downloads for exact-byte checks.

## Measurement Scope and Limitations

- Timing covers `model.generate` after inputs are already on the GPU, including prefill and decoding.
- It excludes retrieval, tokenization, model loading, input transfer, and text decoding.
- GPU synchronization is used around the timed generation.
- Output lengths vary. Output tokens per second is not decode-only speed.
- Memory metrics measure PyTorch tensor allocations, including model allocations, not total GPU usage or reserved memory.
- Requests execute sequentially. Concurrent serving, end-to-end latency, and time to first token were not evaluated.
- Citation presence is not citation support. With no emitted citations, citation precision is undefined.
- The dataset is small and manually authored; semantic grades and gold annotations await human validation.
- The grading rubric was formalized after inspecting test outputs and is retrospective, not preregistered.
- Three timing repetitions do not establish robust statistical significance. No monetary savings or production throughput gains were measured.
- Further changes informed by these test failures must be labelled exploratory or evaluated on a new held-out set.

## Integration Contract

The retrieval pipeline provides records in this format. Expected answers are stored separately and never included in model requests.

```json
{
  "question_id": "q001",
  "policy": "top_k_2",
  "question": "Within how many days can a customer request a refund?",
  "context": "[doc1] Customers can request a refund within 14 days.",
  "source_ids": ["doc1"]
}
```
