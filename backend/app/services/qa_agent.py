from app.services.llm import call_llm

def answer_question(document, question):
    prompt = f"""
    Answer ONLY using the document below.

    Document:
    {document}

    Question:
    {question}
    """

    return call_llm(prompt)