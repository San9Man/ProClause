from fastapi import APIRouter, UploadFile, File
from app.services.pdf_processor import extract_text_from_pdf
from app.services.chunker import split_into_clauses
from app.services.vector_store import create_vector_store
from app.services.rag_agent import answer_query

router = APIRouter()

# store in memory (for now)
global_index = None
global_clauses = None


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global global_index, global_clauses

    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_location)
    clauses = split_into_clauses(text)

    index, stored_clauses = create_vector_store(clauses)

    global_index = index
    global_clauses = stored_clauses

    return {"message": "PDF processed successfully", "clauses": len(clauses)}


@router.post("/ask")
def ask(query: str, persona: str):
    if global_clauses is None:
       return {"error": "Upload a document first"}
  
    answer = answer_query(query, persona, global_index, global_clauses)

    return {"answer": answer}