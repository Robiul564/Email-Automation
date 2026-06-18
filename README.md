# Email Generation Assistant

This project generates professional emails using LLM and evaluates them with 3 custom metrics. It includes two prompting strategies (few-shot vs. no few-shot) for comparison.

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. (Optional) Set OpenAI API key

If you have an OpenAI API key, set it:

```bash
$env:OPENAI_API_KEY = "your_api_key_here"
```

Without an API key, the project runs offline using heuristic evaluation (useful for testing).

## Run the Evaluation

```bash
python run_evaluation.py
```

This generates emails for 10 scenarios and evaluates them with:
- **Model A**: Few-shot prompting + Chain-of-Thought
- **Model B**: Direct prompting (no few-shot examples)

Output files are saved to `output/`:
- `model_a_results.json` — Model A results
- `model_b_results.json` — Model B results  
- `comparison_summary.json` — Head-to-head comparison

## Project Structure

```
Email automation/
├── config/prompts.py           # Prompt template (Few-Shot + CoT)
├── src/
│   ├── email_generator.py      # Generates emails
│   ├── evaluation_metrics.py   # 3 custom metrics
│   └── evaluation_pipeline.py  # Runs evaluation & comparison
├── data/test_scenarios.py      # 10 test scenarios + reference emails
├── output/                     # Results (JSON)
├── run_evaluation.py           # Main runner
└── FINAL_REPORT.md            # Deliverables & analysis
```

## Prompting Strategy: Few-Shot + Chain-of-Thought

Model A uses:
- **Few-Shot Learning**: 2 examples show the model what good emails look like
- **Chain-of-Thought**: Step-by-step reasoning (Analyze Intent → Extract Facts → Assess Tone → Structure → Refine)

## Custom Evaluation Metrics

### Metric 1: Fact Incorporation Score (0-100)
How well all required facts are included and naturally woven into the email.  
**Scoring**: Checks if each key fact appears in the generated email, then uses LLM or keyword matching to verify natural integration.

### Metric 2: Tone Adherence Score (0-100)
How well the email matches the intended tone (formal, casual, urgent, etc.).  
**Scoring**: Analyzes formality level, emotional register, language choices, and consistency throughout the email.

### Metric 3: Professional Quality Score (0-100)
Overall quality: grammar, clarity, structure, and effectiveness.  
**Scoring**: Evaluates opening, body, call-to-action, sentence clarity, and professionalism.

## Test Scenarios (10 total)

1. Follow-up after meeting → Professional, optimistic
2. Request for proposal details → Casual, professional
3. Urgent request → Urgent, direct
4. Express empathy → Empathetic, supportive
5. Announce partnership → Excited, forward-looking
6. Polite rejection → Respectful, diplomatic
7. Schedule meeting → Formal, precise
8. Thank you/gratitude → Warm, grateful
9. Constructive feedback → Constructive, encouraging
10. Organizational announcement → Informative, reassuring
