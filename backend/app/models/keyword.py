from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Keyword(Base):
    __tablename__ = "mots_cles_recherches"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    mot_cle = Column(String, nullable=False)
    volume_recherche = Column(Integer)
    difficulte = Column(Float)
    statut = Column(String, default="nouveau")
    contenu_id = Column(Integer, ForeignKey("contenus.id"), nullable=True)
    date_recherche = Column(TIMESTAMP, server_default="now()")

    client = relationship("Client", back_populates="keywords")
    content = relationship("Content", back_populates="keyword")
    prompts = relationship("PromptHistory", back_populates="keyword")