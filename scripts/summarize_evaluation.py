"""Summarize explicit review labels; never infer semantic grades automatically."""
import argparse
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICIES = ('top_k_8', 'top_k_2', 'budget_900')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--human', action='store_true', help='Require all human review fields.')
    args = parser.parse_args()
    rows = [json.loads(line) for line in (ROOT / 'data/evaluation/test_grades_proposed.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    keys = {(r['question_id'], r['policy']) for r in rows}
    expected = {(f'test_{n:03}', p) for n in range(1, 25) for p in POLICIES}
    if len(rows) != 72 or keys != expected:
        raise ValueError('Expected exactly 24 questions x 3 policies.')
    prefix = 'human' if args.human else 'proposed'
    score_key = prefix + '_correctness_0_2'
    ground_key = prefix + '_grounding'
    abstain_key = prefix + '_abstention_pass'
    for r in rows:
        if args.human and (r['review_status'] != 'human_reviewed' or not r['human_reviewer'].strip()):
            raise ValueError(f"Human review incomplete: {r['question_id']} / {r['policy']}")
        if r['answerable'] and (type(r[score_key]) is not int or r[score_key] not in (0, 1, 2)):
            raise ValueError('Answerable correctness must be an integer 0, 1 or 2.')
        if not r['answerable'] and type(r[abstain_key]) is not bool:
            raise ValueError('Unanswerable abstention must be true or false.')
        if r[ground_key] not in ('supported', 'unsupported_or_contradicted', 'not_applicable'):
            raise ValueError('Invalid grounding label.')
    summary = []
    for p in POLICIES:
        subset = [r for r in rows if r['policy'] == p]
        a = [r for r in subset if r['answerable']]
        u = [r for r in subset if not r['answerable']]
        summary.append({
            'policy': p, 'full_evidence_n_of_18': sum(r['full_evidence_available'] for r in a),
            'fully_correct_n_of_18': sum(r[score_key] == 2 for r in a),
            'partially_correct_n_of_18': sum(r[score_key] == 1 for r in a),
            'incorrect_n_of_18': sum(r[score_key] == 0 for r in a),
            'correctness_points_of_36': sum(r[score_key] for r in a),
            'abstention_n_of_6': sum(r[abstain_key] for r in u),
            'unsupported_or_contradicted_n_of_24': sum(r[ground_key] == 'unsupported_or_contradicted' for r in subset),
            'cited_answerable_n_of_18': sum(r['has_source_citation'] for r in a),
            'distinct_answers_at_cap_n_of_24': sum(r['at_output_cap'] for r in subset),
            'median_of_question_median_seconds': statistics.median(r['median_generation_seconds'] for r in subset),
            'max_peak_allocated_gib': max(r['peak_allocated_gib'] for r in subset),
        })
    reports = ROOT / 'reports'; reports.mkdir(exist_ok=True)
    suffix = 'human' if args.human else 'proposed'
    (reports / f'evaluation_summary_{suffix}.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    lines = [f'# ContextFit evaluation — {suffix}', '',
             'Counts are per distinct question-policy answer. Three timing repetitions are not independent quality samples.', '',
             '| Policy | Full evidence /18 | Correct /18 | Partial /18 | Incorrect /18 | Points /36 | Abstention /6 | Unsupported /24 |',
             '|---|---:|---:|---:|---:|---:|---:|---:|']
    for s in summary:
        lines.append(f"| {s['policy']} | {s['full_evidence_n_of_18']} | {s['fully_correct_n_of_18']} | {s['partially_correct_n_of_18']} | {s['incorrect_n_of_18']} | {s['correctness_points_of_36']} | {s['abstention_n_of_6']} | {s['unsupported_or_contradicted_n_of_24']} |")
    lines += ['', 'Semantic labels follow reports/EVALUATION_RUBRIC.md. Proposed labels are not human-reviewed results.',
              'Unsupported counts include incorrect, contradictory, or ungrounded additions; they are not synonymous with factual hallucination rates.',
              'Citation presence is only a syntactic check; absence does not prove lack of grounding. Citation precision is undefined when there are no citations.',
              'Performance field median_of_question_median_seconds takes the median of 24 within-question medians. It differs from pooling all 72 timing observations.', '']
    (reports / f'evaluation_summary_{suffix}.md').write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))
    print(f'Saved {suffix} evaluation summary.')


if __name__ == '__main__':
    main()
