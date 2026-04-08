from app.services.llm import call_llm

def detect_risk(clause, jurisdiction, persona):
    prompt = f"""
    Analyze this legal clause and identify risks.

    Jurisdiction: {jurisdiction}
    Persona: {persona}

    Return:
    - Risk Level (Low / Medium / High)
    - Reason

    Clause:
    {clause}
    """

    return call_llm(prompt)