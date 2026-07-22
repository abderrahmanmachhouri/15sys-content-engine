from sqlalchemy import Column, Integer, ForeignKey
from pgvector.sqlalchemy import Vector
from sqlalchemy.orm import relationship
from .base import Base


class Embedding(Base):
    __tablename__ = "embeddings"

    id = Column(Integer, primary_key=True, index=True)
    contenu_id = Column(Integer, ForeignKey("contenus.id"), unique=True, nullable=False)
    vecteur = Column(Vector(1536))

    content = relationship("Content", back_populates="embedding")