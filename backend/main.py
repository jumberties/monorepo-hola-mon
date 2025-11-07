from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from db import engine, init_db

app = FastAPI(title="FastAPI + PostgreSQL a Clever Cloud")

# --- Configurar CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producció, posa aquí el domini del frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Endpoint senzill ---
@app.get("/api/message")
def get_message():
    """Retorna el missatge emmagatzemat a la BD."""
    with engine.connect() as conn:
        result = conn.execute(text("SELECT text FROM messages LIMIT 1"))
        row = result.fetchone()
        return {"message": row[0] if row else "No hi ha dades!"}

# --- Inicialitzar base de dades en arrencar ---
@app.on_event("startup")
def on_startup():
    init_db()

