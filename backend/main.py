from fastapi import FastAPI
from sqlalchemy import text

from database import engine

app = FastAPI(title="Empório Gralha Azul")

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/db")
def health_db():
    with engine.connect() as conexao:
        conexao.execute(text("SELECT 1"))
    return {"database": "ok"}