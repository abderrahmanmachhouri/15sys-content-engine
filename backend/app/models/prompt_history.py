from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import Base


class PromptHistory(Base):
    __tablename__ = "prompts_historique"

    id = Column(Integer, primary_key=True, index=True)
    contenu_id = Column(Integer, ForeignKey("contenus.id"), nullable=False)
    mot_cle_id = Column(Integer, ForeignKey("mots_cles_recherches.id"), nullable=True)
    parametres = Column(JSON)
    origine = Column(String)
    score_performance = Column(Float, nullable=True)
    date_creation = Column(TIMESTAMP, server_default="now()")

    content = relationship("Content", back_populates="prompt")
    keyword = relationship("Keyword", back_populates="prompts")