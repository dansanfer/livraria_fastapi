from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import livros
from app.database.connection import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

# Configuração correta e prioritária do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(livros.router)

@app.get("/")
async def home():
    return {"message": "Bem-vindo à API de Livros!"}