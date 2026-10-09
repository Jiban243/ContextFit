# ContextFit evaluation rubric v1

Status: retrospective assistant-proposed rubric and labels. This rubric was formalized after inspecting test outputs; it was not preregistered. All labels require human review. Gold records also remain marked pending in the supplied file. No model outputs or gold labels were changed.

## Units and denominators

24 test questions x 3 policies = 72 distinct answers. Each answer was repeated three times for timing, with identical answer text. Grade each distinct answer once. There are 18 answerable and 6 corpus-unanswerable questions per policy. Test results are conditional on this small, manually authored Python-documentation dataset.

## Correctness for answerable questions

- 2: answers all material parts of the question correctly, without material false additions.
- 1: provides a useful correct part but omits required information, without a central contradiction. Minor filename omissions and incomplete instructions may receive partial credit; explain each decision.
- 0: materially incorrect, contradictory, irrelevant, or fails the requested operation. Correct commands do not automatically rescue a material false explanation.
- null: used for corpus-unanswerable questions, which are scored separately for abstention.

Use expected answer points as the reference, but do not penalize missing explanatory detail that the question does not request (e.g. test_001 only asks for a Python version). Do not silently expand the reference after observing outputs. Borderline rows explicitly mark interpretation choices. No substring or keyword score is used for semantics.

## Grounding

- supported: substantive completed claims follow from supplied context. A partial or irrelevant answer can still be grounded.
- unsupported_or_contradicted: at least one substantive claim is absent from, conflicts with, or overstates supplied context. This includes plausible outside knowledge; this label is not a claim that every such statement is factually false.
- not_applicable: a pure refusal or statement of insufficient information without substantive factual additions.

Incomplete trailing fragments are captured by the token-cap flag rather than assumed to be a claim. A factually correct answer can fail grounding, and an irrelevant quotation can be grounded while failing correctness.

## Abstention for six unanswerable questions

true: acknowledges insufficient information, or clearly says the documentation supplies no requested value, without inventing the value. Unsupported auxiliary advice is handled separately by grounding. false: supplies an unsupported value, answers irrelevantly, or uses an ambiguous fragment that does not clearly express missing information. null: answerable question.

Borderline decisions requiring particular attention:
- test_022 / top_k_8: "No numerical speedup is guaranteed" is provisionally accepted as a denial of a documented guarantee. It is also marked ungrounded for overstating what absence of documentation proves. A stricter explicit-uncertainty rule would reduce this policy's abstention count from 4/6 to 3/6.
- test_022 / top_k_2: "Not applicable" is not accepted as an explicit explanation of insufficient information.
- test_023 / budget_900: "no explicit limit" is read as no specified maximum, so provisionally passes abstention; unsolicited advice fails grounding. If interpreted as an implementation guarantee rather than documentation absence, abstention would fall from 4/6 to 3/6.

## Citations

Presence of a bracketed source marker is an automatic syntactic check. It does not establish supporting evidence or entailment. In this test there are zero source citations under every policy, including 0/18 answerable answers per policy. Citation precision is undefined, not 0% or 100%, because no citations were emitted. Missing citations are not additionally deducted from the correctness score.

## Evidence and truncation

Full evidence available = at least one annotated sufficient evidence set is a subset of selected source_ids. AND within a set; OR between alternative sets. This metric depends on annotation completeness and is not an exhaustive semantic retrieval assessment. It is not defined for unanswerable questions.

At output cap = output_tokens >= 80. A cap hit does not by itself prove truncation; visible incompleteness is assessed in each reason. An early EOS at exactly the limit cannot be distinguished from stored token count alone.

## Human review

Review the question, expected points, complete context, answer, and proposed reason in TEST_ANSWER_REVIEW.md. Keep the proposed fields for audit. In test_grades_proposed.jsonl fill human_correctness_0_2 for answerable questions, human_abstention_pass for unanswerable questions, human_grounding for every row, human_reviewer, and human_notes. Set review_status to human_reviewed only after actual review. Retain null for inapplicable metrics. Then run python scripts/summarize_evaluation.py --human. It refuses incomplete human labels. Review gold annotations separately; reviewing model grades does not automatically certify the gold dataset.
