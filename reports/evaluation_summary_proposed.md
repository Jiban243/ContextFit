# ContextFit evaluation — proposed

Counts are per distinct question-policy answer. Three timing repetitions are not independent quality samples.

| Policy | Full evidence /18 | Correct /18 | Partial /18 | Incorrect /18 | Points /36 | Abstention /6 | Unsupported /24 |
|---|---:|---:|---:|---:|---:|---:|---:|
| top_k_8 | 18 | 7 | 6 | 5 | 20 | 4 | 10 |
| top_k_2 | 16 | 6 | 4 | 8 | 16 | 3 | 13 |
| budget_900 | 17 | 7 | 3 | 8 | 17 | 4 | 14 |

Semantic labels follow reports/EVALUATION_RUBRIC.md. Proposed labels are not human-reviewed results.
Unsupported counts include incorrect, contradictory, or ungrounded additions; they are not synonymous with factual hallucination rates.
Citation presence is only a syntactic check; absence does not prove lack of grounding. Citation precision is undefined when there are no citations.
Performance field median_of_question_median_seconds takes the median of 24 within-question medians. It differs from pooling all 72 timing observations.
