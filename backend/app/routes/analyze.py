from fastapi import APIRouter
from pydantic import BaseModel

from app.services.simplifier import simplify_clause
from app.services.risk_detector import detect_risk
from app.services.recommender import recommend_action

router = APIRouter()

class AnalyzeRequest(BaseModel):
    clause: str
    jurisdiction: str
    persona: str

@router.post("/analyze")
def analyze(data: AnalyzeRequest):
    simplified = simplify_clause(data.clause, data.jurisdiction, data.persona)
    risk = detect_risk(data.clause, data.jurisdiction, data.persona)
    recommendation = recommend_action(data.clause)

    return {
        "original": data.clause,
        "simplified": simplified,
        "risk": risk,
        "recommendation": recommendation
    }