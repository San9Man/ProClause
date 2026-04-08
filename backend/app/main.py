from fastapi import FastAPI
from app.routes import analyze, chat

# CREATE APP FIRST
app = FastAPI()

# ROOT ROUTE (optional)
@app.get("/")
def home():
    return {"message": "Legal AI Agent Running 🚀"}

# INCLUDE ROUTES
app.include_router(analyze.router)
app.include_router(chat.router)