from app.services.llm import call_llm

def recommend_action(clause):
    prompt = f"""
    Suggest what the user should do about this clause.
    Clause: {clause}
    """

    return call_llm(prompt) or "No recommendation available"