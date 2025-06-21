from fastapi import Depends, FastAPI
from typing import List
from . import crud, models, schemas
from .database import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI(title="Notes Service")

# создаю экземпляр приложение с названием Notes Service

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  добавляю зависимость для получения сессии БД


@app.get("/")
def root():
    return {"status": "Working"}
# создаю тело гет реквеста, при вызове которого будет оторбажаться по корневому пути хост/ надпись что микросервис работает


@app.get("/notes/", response_model=List[schemas.Note])
def get_all_notes_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Вызываем функцию из crud.py для получения данных
    notes = crud.get_notes(db, skip=skip, limit=limit)
    return notes

# создаю тело гет реквеста, при вызове которого будет возвращаться база данных с нашими заметками и отображаться запросившему по пути хост/notes


@app.post("/notes/", response_model=schemas.Note)
def create_note_endpoint(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db=db, note=note)

# создаю тело пост запроса для создания заметки





