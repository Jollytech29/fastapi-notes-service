from typing import List
from pydantic import BaseModel
from datetime import datetime


# Глянул, что хорошим тоном является поместить все шаблоны классов в файл schemas.py

class NoteBase(BaseModel):
    title: str
    content: str | None = None
    tags: List[str] = []

# Создаю базовый класс для объектов заметок с полем "название" и ожидаю что оно будет типа str
# "Наполнением" типа str или None, если пользователь или другой микросервис ничего в это поле не сообщает
# Ну и для красоты еще теги прикручиваю которые ожидаются в виде массива

class NoteCreate(NoteBase):
    pass

# Делаю класс дублер для читаемости кода


class Note(NoteBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Делаю еще один класс для использования серваком для формирования ответа клиенту, который будет помимо title, content и tags ожидать еще и заполнения от сервака "id" типа int и "даты создания" типа datatime
