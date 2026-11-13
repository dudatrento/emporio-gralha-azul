from fastapi import FastAPI

app = FastAPI(title="Empório Gralha Azul")

@app.get("/health")
def health():
    return {"status": "ok"}
