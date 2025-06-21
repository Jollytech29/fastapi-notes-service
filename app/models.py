from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Note(Base):
# создаю класс-сущность Note с описанием таблицы "notes" c помощью SQLAlchemy
# глянул в инете, что такие классы создаем в models.py
    __tablename__ = "notes"
    # указываю имя таблицы

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, nullable=True)
    tags = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # описываю колонки и поля таблицы
