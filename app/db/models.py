from sqlalchemy import Column, Integer, Text
from pgvector.sqlalchemy import Vector

from app.db.database import Base


class Show(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    overview = Column(Text)
    embedding = Column(Vector(384))