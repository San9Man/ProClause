def split_into_clauses(text):
    clauses = text.split("\n")
    cleaned = [c.strip() for c in clauses if len(c.strip()) > 30]
    return cleaned