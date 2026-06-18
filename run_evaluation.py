"""
Run evaluation for two strategies and save outputs.
Model A: Few-shot + default model
Model B: No few-shot (different prompting strategy)

Usage:
    python run_evaluation.py

If OPENAI_API_KEY is set, this will use the OpenAI client; otherwise runs in offline heuristic mode.
"""

from src.evaluation_pipeline import EvaluationPipeline, ModelComparator
from data.test_scenarios import get_test_scenarios
import json


def main():
    scenarios = get_test_scenarios()

    # Model A: include few-shot examples
    pipeline_a = EvaluationPipeline(api_key=None)  # set env OPENAI_API_KEY to use remote
    pipeline_a.generator.offline = pipeline_a.generator.offline  # preserve
    print("Running Model A (Few-shot)")
    # Force include_few_shot True inside generator calls by temporarily wrapping generate_email
    results_a = []
    for s in scenarios:
        gen = pipeline_a.generator.generate_email(
            intent=s["intent"],
            key_facts=s["key_facts"],
            tone=s["tone"],
            include_few_shot=True
        )
        eval_res = pipeline_a.evaluator.evaluate_email(
            generated_email=gen,
            intent=s["intent"],
            key_facts=s["key_facts"],
            tone=s["tone"],
            reference_email=s.get("reference_email")
        )
        results_a.append({
            "scenario_id": s["scenario_id"],
            "generated_email": gen,
            "evaluation": eval_res
        })

    pipeline_a.results = [
        {
            "scenario_id": r["scenario_id"],
            "intent": s["intent"],
            "tone": s["tone"],
            "key_facts": s["key_facts"],
            "reference_email": s.get("reference_email", ""),
            "generated_email": r["generated_email"],
            "model_name": "Model A",
            "overall_score": r["evaluation"]["overall_score"],
            "metric_1_fact_incorporation": r["evaluation"]["metric_1_fact_incorporation"],
            "metric_2_tone_adherence": r["evaluation"]["metric_2_tone_adherence"],
            "metric_3_professional_quality": r["evaluation"]["metric_3_professional_quality"],
            "evaluation_timestamp": ""
        }
        for r, s in zip(results_a, scenarios)
    ]

    # Model B: same model but no few-shot examples (different prompting strategy)
    pipeline_b = EvaluationPipeline(api_key=None)
    print("Running Model B (No few-shot)")
    results_b = []
    for s in scenarios:
        gen = pipeline_b.generator.generate_email(
            intent=s["intent"],
            key_facts=s["key_facts"],
            tone=s["tone"],
            include_few_shot=False
        )
        eval_res = pipeline_b.evaluator.evaluate_email(
            generated_email=gen,
            intent=s["intent"],
            key_facts=s["key_facts"],
            tone=s["tone"],
            reference_email=s.get("reference_email")
        )
        results_b.append({
            "scenario_id": s["scenario_id"],
            "generated_email": gen,
            "evaluation": eval_res
        })

    pipeline_b.results = [
        {
            "scenario_id": r["scenario_id"],
            "intent": s["intent"],
            "tone": s["tone"],
            "key_facts": s["key_facts"],
            "reference_email": s.get("reference_email", ""),
            "generated_email": r["generated_email"],
            "model_name": "Model B",
            "overall_score": r["evaluation"]["overall_score"],
            "metric_1_fact_incorporation": r["evaluation"]["metric_1_fact_incorporation"],
            "metric_2_tone_adherence": r["evaluation"]["metric_2_tone_adherence"],
            "metric_3_professional_quality": r["evaluation"]["metric_3_professional_quality"],
            "evaluation_timestamp": ""
        }
        for r, s in zip(results_b, scenarios)
    ]

    # Save outputs
    with open('output/model_a_results.json', 'w', encoding='utf-8') as f:
        json.dump(pipeline_a.results, f, indent=2, ensure_ascii=False)
    with open('output/model_b_results.json', 'w', encoding='utf-8') as f:
        json.dump(pipeline_b.results, f, indent=2, ensure_ascii=False)

    # Comparison
    comparator = ModelComparator()
    comparison = comparator.compare_models(pipeline_a.results, pipeline_b.results)
    with open('output/comparison_summary.json', 'w', encoding='utf-8') as f:
        json.dump(comparison, f, indent=2, ensure_ascii=False)

    print('Evaluation complete. Results saved to output/*.json')


if __name__ == '__main__':
    main()
