from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import Base


class Metric(Base):
    __tablename__ = "metriques"

    id = Column(Integer, primary_key=True, index=True)
    contenu_id = Column(Integer, ForeignKey("contenus.id"), nullable=False)
    plateforme = Column(String, nullable=False)
    vues = Column(Integer, default=0)
    donnees_specifiques = Column(JSON)
    date_mesure = Column(TIMESTAMP, server_default="now()")

    content = relationship("Content", back_populates="metrics")