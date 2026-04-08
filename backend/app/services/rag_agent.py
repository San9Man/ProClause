def answer_query(query, persona, index, clauses):
    
    # Take top 3 clauses
    relevant_clauses = clauses[:3]

    context = "\n".join(relevant_clauses)

    # 🧠 SMART RULE-BASED RESPONSE
    answer = ""

    if "terminate" in context.lower() or "evict" in query.lower():
        answer += "⚠️ Risk: The landlord may remove you without warning.\n\n"

    if "payment" in context.lower():
        answer += "💰 Obligation: You must pay on time to avoid penalties.\n\n"

    if "liability" in context.lower():
        answer += "⚠️ Risk: You may be responsible for damages.\n\n"

    # Always include explanation
    answer += "📄 Simple Explanation:\n"
    answer += "This clause means the agreement gives one party strong control.\n\n"

    answer += "💡 Recommendation:\n"
    answer += "You should review this clause carefully and negotiate better terms if possible."

    return answer