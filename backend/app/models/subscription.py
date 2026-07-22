from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Subscription(Base):
    __tablename__ = "abonnements"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), unique=True, nullable=False)
    date_debut = Column(TIMESTAMP, nullable=False)
    date_fin = Column(TIMESTAMP, nullable=True)
    statut = Column(String, default="actif")

    client = relationship("Client", back_populates="subscription")