"""
Main Evaluation Pipeline
Runs email generation and evaluation for all test scenarios
Supports comparison between two models/strategies
"""

import json
import csv
import os
from datetime import datetime
from src.email_generator import EmailGenerator
from src.evaluation_metrics import EmailEvaluator
from data.test_scenarios import get_test_scenarios


class EvaluationPipeline:
    """Runs complete evaluation pipeline for email generation."""
    
    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        """Initialize pipeline with generator and evaluator."""
        self.api_key = api_key
        self.model = model
        self.generator = EmailGenerator(api_key=api_key, model=model)
        self.evaluator = EmailEvaluator(api_key=api_key, model=model)
        self.results = []
    
    def run_evaluation(self, scenarios=None, model_name="Model A"):
        """
        Run evaluation on all scenarios.
        
        Args:
            scenarios: List of scenarios (uses default if None)
            model_name: Name of the model being evaluated
        
        Returns:
            List of evaluation results
        """
        if scenarios is None:
            scenarios = get_test_scenarios()
        
        results = []
        
        for i, scenario in enumerate(scenarios, 1):
            print(f"\n{'='*70}")
            print(f"Evaluating Scenario {i}/10: {scenario['intent']}")
            print(f"{'='*70}")
            
            # Generate email
            print("Generating email...")
            generated_email = self.generator.generate_email(
                intent=scenario["intent"],
                key_facts=scenario["key_facts"],
                tone=scenario["tone"],
                include_few_shot=True
            )
            
            print("Evaluating email...")
            # Evaluate email
            evaluation = self.evaluator.evaluate_email(
                generated_email=generated_email,
                intent=scenario["intent"],
                key_facts=scenario["key_facts"],
                tone=scenario["tone"],
                reference_email=scenario.get("reference_email")
            )
            
            # Compile result
            result = {
                "scenario_id": scenario["scenario_id"],
                "intent": scenario["intent"],
                "tone": scenario["tone"],
                "key_facts": scenario["key_facts"],
                "reference_email": scenario.get("reference_email", ""),
                "generated_email": generated_email,
                "model_name": model_name,
                "overall_score": evaluation["overall_score"],
                "metric_1_fact_incorporation": evaluation["metric_1_fact_incorporation"],
                "metric_2_tone_adherence": evaluation["metric_2_tone_adherence"],
                "metric_3_professional_quality": evaluation["metric_3_professional_quality"],
                "evaluation_timestamp": datetime.now().isoformat()
            }
            
            results.append(result)
            
            # Print summary
            print(f"\n--- Evaluation Summary ---")
            print(f"Overall Score: {evaluation['overall_score']:.1f}/100")
            print(f"Fact Incorporation: {evaluation['metric_1_fact_incorporation']['score']:.1f}/100")
            print(f"Tone Adherence: {evaluation['metric_2_tone_adherence']['score']:.1f}/100")
            print(f"Professional Quality: {evaluation['metric_3_professional_quality']['score']:.1f}/100")
        
        self.results = results
        return results
    
    def save_results_json(self, filename=None):
        """Save results to JSON file."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"output/evaluation_results_{timestamp}.json"
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        print(f"\nResults saved to {filename}")
        return filename
    
    def save_results_csv(self, filename=None):
        """Save summary results to CSV file."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"output/evaluation_summary_{timestamp}.csv"
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow([
                "Scenario ID",
                "Intent",
                "Tone",
                "Model",
                "Overall Score",
                "Fact Incorporation",
                "Tone Adherence",
                "Professional Quality",
                "Fact Coverage %",
                "Timestamp"
            ])
            
            # Write data rows
            for result in self.results:
                writer.writerow([
                    result["scenario_id"],
                    result["intent"],
                    result["tone"],
                    result["model_name"],
                    round(result["overall_score"], 2),
                    round(result["metric_1_fact_incorporation"]["score"], 2),
                    round(result["metric_2_tone_adherence"]["score"], 2),
                    round(result["metric_3_professional_quality"]["score"], 2),
                    round(result["metric_1_fact_incorporation"]["fact_coverage_percent"], 2),
                    result["evaluation_timestamp"]
                ])
        
        print(f"Summary saved to {filename}")
        return filename
    
    def generate_report(self):
        """Generate summary statistics report."""
        if not self.results:
            print("No results to report. Run evaluation first.")
            return
        
        overall_scores = [r["overall_score"] for r in self.results]
        metric_1_scores = [r["metric_1_fact_incorporation"]["score"] for r in self.results]
        metric_2_scores = [r["metric_2_tone_adherence"]["score"] for r in self.results]
        metric_3_scores = [r["metric_3_professional_quality"]["score"] for r in self.results]
        
        avg_overall = sum(overall_scores) / len(overall_scores)
        avg_metric_1 = sum(metric_1_scores) / len(metric_1_scores)
        avg_metric_2 = sum(metric_2_scores) / len(metric_2_scores)
        avg_metric_3 = sum(metric_3_scores) / len(metric_3_scores)
        
        report = {
            "model_name": self.results[0]["model_name"],
            "total_scenarios": len(self.results),
            "evaluation_timestamp": datetime.now().isoformat(),
            "average_scores": {
                "overall": avg_overall,
                "metric_1_fact_incorporation": avg_metric_1,
                "metric_2_tone_adherence": avg_metric_2,
                "metric_3_professional_quality": avg_metric_3
            },
            "metric_1_definition": {
                "name": "Fact Incorporation Score",
                "focus": "Specificity, Information Completeness, Fact Recall",
                "logic": "Measures how well all required key facts are seamlessly incorporated into the email. Uses LLM as judge for semantic matching."
            },
            "metric_2_definition": {
                "name": "Tone Adherence Score",
                "focus": "Tone Accuracy, Format Adherence, Consistency",
                "logic": "Analyzes linguistic patterns and emotional register to judge tone alignment with intended tone."
            },
            "metric_3_definition": {
                "name": "Professional Quality Score",
                "focus": "Grammar/Fluency, Introduction Effectiveness, Conciseness",
                "logic": "Measures overall professional quality including clarity, structure, grammar, and call-to-action effectiveness."
            },
            "detailed_results": self.results
        }
        
        return report
    
    def print_report(self):
        """Print summary report to console."""
        report = self.generate_report()
        
        print("\n" + "="*70)
        print("EMAIL GENERATION EVALUATION REPORT")
        print("="*70)
        print(f"Model: {report['model_name']}")
        print(f"Timestamp: {report['evaluation_timestamp']}")
        print(f"Total Scenarios Evaluated: {report['total_scenarios']}")
        
        print("\n--- AVERAGE SCORES ---")
        print(f"Overall Score: {report['average_scores']['overall']:.2f}/100")
        print(f"Metric 1 (Fact Incorporation): {report['average_scores']['metric_1_fact_incorporation']:.2f}/100")
        print(f"Metric 2 (Tone Adherence): {report['average_scores']['metric_2_tone_adherence']:.2f}/100")
        print(f"Metric 3 (Professional Quality): {report['average_scores']['metric_3_professional_quality']:.2f}/100")
        
        print("\n--- METRICS DEFINITIONS ---")
        for i, metric_key in enumerate(
            ["metric_1_definition", "metric_2_definition", "metric_3_definition"], 1
        ):
            metric = report[metric_key]
            print(f"\nMetric {i}: {metric['name']}")
            print(f"  Focus: {metric['focus']}")
            print(f"  Logic: {metric['logic']}")
        
        print("\n" + "="*70)


class ModelComparator:
    """Compare results between two models."""
    
    @staticmethod
    def compare_models(results_model_a, results_model_b):
        """
        Compare two sets of evaluation results.
        
        Args:
            results_model_a: Results from first model
            results_model_b: Results from second model
        
        Returns:
            Comparison analysis dict
        """
        # Calculate averages
        avg_a = {
            "overall": sum(r["overall_score"] for r in results_model_a) / len(results_model_a),
            "metric_1": sum(r["metric_1_fact_incorporation"]["score"] for r in results_model_a) / len(results_model_a),
            "metric_2": sum(r["metric_2_tone_adherence"]["score"] for r in results_model_a) / len(results_model_a),
            "metric_3": sum(r["metric_3_professional_quality"]["score"] for r in results_model_a) / len(results_model_a),
        }
        
        avg_b = {
            "overall": sum(r["overall_score"] for r in results_model_b) / len(results_model_b),
            "metric_1": sum(r["metric_1_fact_incorporation"]["score"] for r in results_model_b) / len(results_model_b),
            "metric_2": sum(r["metric_2_tone_adherence"]["score"] for r in results_model_b) / len(results_model_b),
            "metric_3": sum(r["metric_3_professional_quality"]["score"] for r in results_model_b) / len(results_model_b),
        }
        
        # Determine winner for each metric
        winner = {
            "overall": "Model A" if avg_a["overall"] > avg_b["overall"] else "Model B",
            "metric_1": "Model A" if avg_a["metric_1"] > avg_b["metric_1"] else "Model B",
            "metric_2": "Model A" if avg_a["metric_2"] > avg_b["metric_2"] else "Model B",
            "metric_3": "Model A" if avg_a["metric_3"] > avg_b["metric_3"] else "Model B",
        }
        
        return {
            "model_a_averages": avg_a,
            "model_b_averages": avg_b,
            "winners": winner,
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def print_comparison(comparison):
        """Print comparison results."""
        print("\n" + "="*70)
        print("MODEL COMPARISON REPORT")
        print("="*70)
        
        print("\n--- AVERAGE SCORES ---")
        print(f"{'Metric':<30} {'Model A':<20} {'Model B':<20} {'Winner':<15}")
        print("-" * 85)
        
        metrics = [
            ("Overall Score", "overall"),
            ("Fact Incorporation", "metric_1"),
            ("Tone Adherence", "metric_2"),
            ("Professional Quality", "metric_3")
        ]
        
        for metric_name, metric_key in metrics:
            a_score = comparison["model_a_averages"][metric_key]
            b_score = comparison["model_b_averages"][metric_key]
            winner = comparison["winners"][metric_key]
            print(f"{metric_name:<30} {a_score:<20.2f} {b_score:<20.2f} {winner:<15}")
        
        print("\n" + "="*70)
