def answer_query(query, persona, index, clauses):
    if not clauses:
        return {
            "risk_level": "UNKNOWN",
            "explanation": "No document uploaded.",
            "obligations": [],
            "recommendation": "Upload a document first."
        }

    # pick a few clauses
    relevant_clauses = clauses[:3]
    context = " ".join(relevant_clauses).lower()
    q = query.lower()

    risk_level = "LOW"
    explanation = ""
    obligations = []
    recommendation = "Review carefully and negotiate safer terms if needed."

    # ---- simple intent + rule checks ----
    if "terminate" in context or "evict" in q:
        risk_level = "HIGH"
        explanation += "The agreement allows termination without notice. "
        recommendation = "Ask for notice period or protection before termination."

    if "payment" in context:
        obligations.append("You must pay on time to avoid penalties.")

    if "liability" in context:
        risk_level = "HIGH"
        obligations.append("You may be responsible for damages.")

    if not explanation:
        explanation = "This clause defines responsibilities and rights between parties."

    return {
        "risk_level": risk_level,
        "explanation": explanation.strip(),
        "obligations": obligations,
        "recommendation": recommendation
    }