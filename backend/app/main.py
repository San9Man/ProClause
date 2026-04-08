from fastapi import FastAPI
from app.routes import analyze, chat

app = FastAPI()

app.include_router(analyze.router)
app.include_router(chat.router)

@app.get("/")
def home():
    return {"message": "Legal AI Agent Running 🚀"}