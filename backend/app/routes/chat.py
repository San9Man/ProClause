from fastapi import APIRouter
from pydantic import BaseModel

from app.services.qa_agent import answer_question

router = APIRouter()

class ChatRequest(BaseModel):
    document: str
    question: str

@router.post("/chat")
def chat(data: ChatRequest):
    answer = answer_question(data.document, data.question)

    return {"answer": answer}