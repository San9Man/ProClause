from openai import OpenAI
from app.config import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def simplify_clause(clause, jurisdiction, persona):
    prompt = f"""
    Explain this legal clause in simple English.
    Jurisdiction: {jurisdiction}
    Persona: {persona}

    Clause:
    {clause}
    """

    response = client.chat.completions.create(
        model="mistralai/mixtral-8x7b-instruct",  # IMPORTANT
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.contentgive