"""
Email Generation Assistant using OpenAI API
"""

import os
from openai import OpenAI
from config.prompts import get_system_prompt, format_prompt


class EmailGenerator:
    """
    Generates professional emails using OpenAI's GPT models.
    """
    
    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        """
        Initialize the email generator.
        
        Args:
            api_key: OpenAI API key (uses OPENAI_API_KEY env var if not provided)
            model: OpenAI model to use (default: gpt-3.5-turbo)
        """
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        self.system_prompt = get_system_prompt()

        if api_key:
            # Remote LLM mode
            self.client = OpenAI(api_key=api_key)
            self.offline = False
        else:
            # Fallback simple template-based generator for offline use
            self.client = None
            self.offline = True
    
    def generate_email(self, intent, key_facts, tone, include_few_shot=True):
        """
        Generate a professional email based on inputs.
        
        Args:
            intent: The core purpose of the email
            key_facts: List of key facts to include
            tone: The desired tone/style
            include_few_shot: Whether to use few-shot prompting
        
        Returns:
            Generated email string
        """
        # Format the prompt
        user_prompt = format_prompt(intent, key_facts, tone, include_few_shot)
        
        # If offline, use a simple deterministic template-based generator
        if self.offline:
            opening = "Dear [Recipient],\n\n"
            body_lines = []
            # Intro sentence based on intent
            body_lines.append(f"I am writing regarding: {intent}.")
            # Integrate key facts naturally
            for fact in key_facts:
                body_lines.append(fact + ".")

            # Tone marker
            tone_line = f"Tone: {tone}."

            # Call to action based on intent
            cta = "Please let me know if you have any questions or need further details."

            closing = "\nBest regards,\n[Your Name]"

            email = opening + "\n".join(body_lines) + "\n\n" + tone_line + "\n\n" + cta + closing
            return email

        # Call OpenAI API
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        return response.choices[0].message.content.strip()
    
    def batch_generate(self, scenarios):
        """
        Generate emails for multiple scenarios.
        
        Args:
            scenarios: List of dicts with 'intent', 'key_facts', 'tone' keys
        
        Returns:
            List of generated emails
        """
        results = []
        for i, scenario in enumerate(scenarios):
            email = self.generate_email(
                intent=scenario["intent"],
                key_facts=scenario["key_facts"],
                tone=scenario["tone"]
            )
            results.append({
                "scenario_id": i + 1,
                "input": scenario,
                "generated_email": email
            })
        
        return results
