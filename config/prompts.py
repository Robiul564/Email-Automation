SYSTEM_PROMPT = """You are an expert professional email writer with 20 years of experience.
Your task is to generate professional emails that are clear, concise, and impactful.

When generating an email, you MUST follow this exact process (think step by step):

1. ANALYZE the Intent: What is the core purpose of this email?
2. EXTRACT Key Facts: Which critical information must be included?
3. ASSESS the Tone: What emotional register and formality level should this have?
4. STRUCTURE: Create a logical flow with:
   - Professional opening
   - Context/body with all key facts naturally integrated
   - Clear call-to-action
   - Professional closing
5. REFINE: Ensure the tone matches exactly and all facts are present

Always format emails with proper structure and spacing."""

FEW_SHOT_EXAMPLES = """
EXAMPLE 1:
Input:
  Intent: Follow up after initial meeting
  Key Facts: 
    - Discussed project timeline of 6 months
    - Budget approved at $50,000
    - Next milestone is design phase
  Tone: Professional and optimistic

Output:
Dear [Recipient],

Thank you for taking the time to meet with me yesterday. I appreciated our discussion about the project direction.

As we agreed, the project timeline has been set for 6 months with an approved budget of $50,000. I wanted to confirm that our next milestone—the design phase—is scheduled to begin next Monday.

I am enthusiastic about moving forward and confident this project will deliver excellent results. Please let me know if you need any additional information or have any questions.

Best regards,
[Your Name]

---

EXAMPLE 2:
Input:
  Intent: Request for proposal details
  Key Facts:
    - Submitted proposal 2 weeks ago
    - Awaiting client feedback
    - Decision needed by end of month
  Tone: Casual yet professional

Output:
Hi [Recipient],

Hope you're doing well! I wanted to touch base about the proposal I sent over two weeks ago.

I understand these things take time to review, but we want to make sure everything is clear. Is there anything from the proposal you'd like us to clarify? Also, just to confirm, we're looking to have your feedback by month-end so we can move things forward.

Let me know if you have any questions or need anything from our end!

Cheers,
[Your Name]
"""

PROMPT_TEMPLATE = """You are an expert professional email writer. Generate a high-quality professional email based on these inputs.

{few_shot_section}

Now, generate an email for this request:

Intent: {intent}
Key Facts:
{key_facts_formatted}
Tone: {tone}

IMPORTANT: 
- Include ALL key facts naturally within the email body
- Match the specified tone exactly
- Use professional structure with clear opening, body, and closing
- Do not include the recipient name in the body (use [Recipient] placeholder)
- Do not add meta-commentary or explanations
- Output ONLY the email itself, ready to send

Generate the email now:"""


def get_system_prompt():
    """Returns the system prompt for the assistant."""
    return SYSTEM_PROMPT


def get_few_shot_examples():
    """Returns few-shot learning examples."""
    return FEW_SHOT_EXAMPLES


def format_prompt(intent, key_facts, tone, include_few_shot=True):
    """
    Format the complete prompt for email generation.
    
    Args:
        intent: The core purpose of the email
        key_facts: List of key facts to include
        tone: The desired tone/style
        include_few_shot: Whether to include few-shot examples
    
    Returns:
        Formatted prompt string
    """
    few_shot_section = get_few_shot_examples() if include_few_shot else ""
    
    # Format key facts as a bulleted list
    key_facts_formatted = "\n".join([f"  - {fact}" for fact in key_facts])
    
    prompt = PROMPT_TEMPLATE.format(
        few_shot_section=few_shot_section,
        intent=intent,
        key_facts_formatted=key_facts_formatted,
        tone=tone
    )
    
    return prompt
