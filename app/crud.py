from sqlalchemy.orm import Session
from . import models, schemas

def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()

# создаю функцию для получения заметок



def create_note(db: Session, note: schemas.NoteCreate):
    tags_as_string = ",".join(note.tags) if note.tags else ""

# создаю функцию для создания заметки

    db_note = models.Note(
        title=note.title,
        content=note.content,
        tags=tags_as_string
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note