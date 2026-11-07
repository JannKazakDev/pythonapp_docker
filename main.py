from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Docker Practice App")

# Временное хранилище в памяти
notes_db = []

class Note(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": " Приложение успешно работает"}

@app.get("/health")
def health_check():
    return {"status": "пашет"}

@app.get("/notes")
def get_notes():
    return {"notes": notes_db}

@app.post("/notes")
def add_note(note: Note):
    notes_db.append(note.text)
    return {"message": "Заметка добавленa", "notes": notes_db}