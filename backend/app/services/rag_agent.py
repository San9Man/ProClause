from app.services.llm import call_llm

def answer_query(query, persona, index, clauses):
    
  
    relevant_clauses = clauses[:3]

    context = "\n".join(relevant_clauses)

    prompt = f"""
You are a legal assistant.

User Persona: {persona}

Use ONLY the provided clauses to answer.

Context:
{context}

Question:
{query}

Instructions:
- Explain in simple English
- Identify risks for the {persona}
- Suggest actions
"""

    return call_llm(prompt)