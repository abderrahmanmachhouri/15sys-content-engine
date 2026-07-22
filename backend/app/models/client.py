from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), unique=True, nullable=False)
    secteur_activite = Column(String)
    specialite = Column(String)
    zone_geographique = Column(String)
    nom_sous_domaine = Column(String, unique=True)
    statut_abonnement = Column(String, default="inactif")

    user = relationship("User", back_populates="client")
    contents = relationship("Content", back_populates="client")
    keywords = relationship("Keyword", back_populates="client")
    social_connections = relationship("SocialConnection", back_populates="client")
    subscription = relationship("Subscription", back_populates="client", uselist=False)