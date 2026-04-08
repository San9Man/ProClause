from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import analyze, chat

# CREATE APP FIRST
app = FastAPI()

# Enable CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROOT ROUTE (optional)
@app.get("/")
def home():
    return {"message": "Legal AI Agent Running 🚀"}

# INCLUDE ROUTES
app.include_router(analyze.router)
app.include_router(chat.router)