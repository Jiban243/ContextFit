# ContextFit: T4 context-policy experiment

Status: measured performance and assistant-proposed answer grades. Human validation pending.

## Problem and scope

A retrieval-augmented assistant sends retrieved text to a GPU-hosted language model. Additional context can preserve evidence while increasing prompt processing and memory use. ContextFit measures this trade-off for three simple selection policies. It is an application-level GPU inference experiment, not a CUDA kernel optimization or production deployment benchmark.

## Setup

Three Python tutorial snapshots, 50 chunks (maximum 300 tokens), BM25 retrieval with ten candidates per question. Compare the first eight chunks, first two chunks, and greedy whole-chunk inclusion under a 900-context-token budget. Markers count toward the context budget; instructions and the question explain why complete prompts exceed 900 tokens. Policies share the candidate ranking for each question.

Model: Qwen/Qwen2.5-1.5B-Instruct; Tesla T4; float16; SDPA; greedy generation; maximum 80 output tokens; project input cap 4016. Logged environment: Python 3.13.15, PyTorch 2.11.0+cu130, Transformers 5.18.0, CUDA 13.0. Model revision was logged as null, so an exact model snapshot is not pinned in these records.

Six development questions preceded 24 test questions (18 answerable, six unanswerable). No prompt or output-limit change was made between the supplied development and test runs. Three sequential repetitions per question-policy pair were shuffled by the runner with seed 42. Warm-up was excluded. There are 216 successful unique test jobs and identical generated answer text across repetitions for each of the 72 pairs.

## Measured resources

| Policy | Median input tokens | Median output tokens | Pooled median generation seconds | Maximum peak allocated GiB | Cap-reaching generations /72 |
|---|---:|---:|---:|---:|---:|
| top_k_8 | 2235.0 | 36.0 | 2.335 | 3.651 | 9 |
| top_k_2 | 627.5 | 43.5 | 1.691 | 2.974 | 6 |
| budget_900 | 910.5 | 51.0 | 2.147 | 3.044 | 9 |

Against top_k_8, pooled median generation time is about 27.6% lower for top_k_2 and 8.1% lower for budget_900. Maximum observed peak allocated memory is about 18.5% and 16.6% lower respectively. These are descriptive comparisons, not statistically established general speedups.

Generation time includes prefill and decoding, excludes retrieval, tokenization, and transfer before generate(), and uses CUDA synchronization. Output lengths differ, so timings do not isolate input-context processing cost. Peak allocated memory includes model allocations and is not total device memory, reserved memory, or guaranteed serving capacity. No monetary savings, concurrency gains, or production throughput were measured.

## Proposed quality assessment

| Policy | Full annotated evidence /18 | Fully correct /18 | Partial /18 | Incorrect /18 | Correctness points /36 | Abstention /6 | Unsupported or contradicted answers /24 |
|---|---:|---:|---:|---:|---:|---:|---:|
| top_k_8 | 18 | 7 | 6 | 5 | 20 | 4 | 10 |
| top_k_2 | 16 | 6 | 4 | 8 | 16 | 3 | 13 |
| budget_900 | 17 | 7 | 3 | 8 | 17 | 4 | 14 |

All semantic scores above are assistant proposals under EVALUATION_RUBRIC.md, not human-reviewed accuracy. The two 4/6 abstention counts each include one borderline interpretation; a stricter interpretation makes either 3/6. There are zero source citations for every policy (0/18 answerable answers). No citation precision can be calculated because no citations were emitted.

The summary script regenerates quality counts from individual labels. It also reports a median of within-question timing medians, explicitly named differently from the pooled median shown above. Do not mix these aggregations in percentage claims.

## Failure analysis

- Retrieval evidence: top_k_2 misses complete annotated evidence for test_014 (upgrade and export versions) and test_018 (selective exception-group handling). budget_900 misses complete evidence for test_018. top_k_8 includes a sufficient annotated set for all 18 answerable questions.
- Generation despite available evidence: all three policies get the execution-vs-loading distinction wrong in test_008 and explicit exception causes wrong in test_017. More context does not automatically fix interpretation.
- Instruction completion: all three test_013 responses stop before finishing environment creation, activation and dependency installation. The 80-token cap and verbose output prevent complete answers.
- Grounding vs knowledge: test_024 promotes a historical documentation example (2.7.0) to the current latest Requests release. The corpus cannot establish a current latest version; no external version lookup is needed to identify that unsupported inference.
- Citation compliance: all 72 answers lack source citations despite prompt instructions.
- Abstention: several answers refuse unknown values correctly, but append unsupported advice. Record abstention and grounding separately rather than equating any refusal phrase with a fully safe answer.

## Interpretation and business relevance

This experiment demonstrates a way to measure whether reducing retrieved context saves GPU resources at an acceptable quality cost. top_k_2 has the lowest observed pooled median generation time and peak allocation, but loses annotated evidence on two answerable questions and has fewer proposed fully correct answers than top_k_8. budget_900 preserves more evidence than top_k_2 but does not dominate other policies across speed and quality. None is ready for a citation-dependent production assistant under these settings.

The defensible outcome is a benchmark and a diagnosis: context selection can reduce measured resource use, while generation quality remains a separate bottleneck. There is no demonstrated production cost reduction or universal best policy.

## Limits and next experiments

The corpus and question set are small, manually authored and confined to one domain. Development and test share source documents and concepts; this is not cross-domain generalization. Three repeated timings per question do not constitute 72 independent quality samples. Colab timing variation, changing output lengths, and lack of isolated prefill/decoding timing limit performance attribution. Gold annotations remain pending human review. The semantic rubric was formalized after inspecting test answers, so it is retrospective and potentially biased.

Future experiments can use development data to compare a concise citation-focused prompt and larger output budget, then evaluate once on a new held-out question set. Increasing output allowance also requires updating input reservation and exporter checks consistently. Preserve this baseline. Test-set-informed changes must be labeled exploratory or evaluated on new held-out data.
