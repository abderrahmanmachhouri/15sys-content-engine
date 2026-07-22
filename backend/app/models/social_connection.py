from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class SocialConnection(Base):
    __tablename__ = "reseaux_sociaux_connexions"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    plateforme = Column(String, nullable=False)
    access_token = Column(Text)
    expire_le = Column(TIMESTAMP)
    date_connexion = Column(TIMESTAMP, server_default="now()")

    client = relationship("Client", back_populates="social_connections")