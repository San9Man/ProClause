from app.services.llm import call_llm

def detect_risk(clause, jurisdiction, persona):
    prompt = f"""
    Identify risk in this clause and classify as Low, Medium, or High.
    Clause: {clause}
    """

    return call_llm(prompt) or "Risk analysis unavailable"