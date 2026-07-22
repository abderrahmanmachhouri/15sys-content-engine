from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from .base import Base


class Content(Base):
    __tablename__ = "contenus"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    type = Column(String, nullable=False)
    titre = Column(String)
    slug = Column(String, unique=True)
    contenu = Column(Text, nullable=False)
    tags = Column(ARRAY(String))
    image = Column(String)
    date_creation = Column(TIMESTAMP, server_default="now()")
    date_publication = Column(TIMESTAMP)
    date_validation = Column(TIMESTAMP)

    client = relationship("Client", back_populates="contents")
    metrics = relationship("Metric", back_populates="content")
    prompt = relationship("PromptHistory", back_populates="content", uselist=False)
    embedding = relationship("Embedding", back_populates="content", uselist=False)
    keyword = relationship("Keyword", back_populates="content")