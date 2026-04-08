from app.services.llm import call_llm

def simplify_clause(clause, jurisdiction, persona):
    prompt = f"""
    Explain this legal clause in simple English.
    Clause: {clause}
    """

    return call_llm(prompt) or "Could not simplify clause"