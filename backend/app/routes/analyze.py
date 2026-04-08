from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze")
def analyze_clause(data: dict):
    clause = data.get("clause", "")

    simplified = f"This means: {clause}"

    risk = "⚠️ Risk: This clause may give one party too much power."

    recommendation = "💡 Recommendation: Review and negotiate this clause."

    return {
        "original": clause,
        "simplified": simplified,
        "risk": risk,
        "recommendation": recommendation
    }