from app.services.llm import call_llm

def recommend_action(clause):
    prompt = f"""
    Suggest 2-3 actions the user should take based on this clause.

    Clause:
    {clause}
    """

    return call_llm(prompt)