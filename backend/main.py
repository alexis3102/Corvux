from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# main.py está en Corvux/backend/main.py
BASE_DIR = Path(__file__).resolve().parent.parent   # sube dos niveles: backend → Corvux
FRONTEND_DIR = BASE_DIR / "frontend"                # entra a Corvux/frontend

app = FastAPI()


@app.get("/api/hello")
def read_root():
    return {"message": "hello Corvux"}


# Siempre al final: todo lo que no sea /api lo atiende el frontend
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")