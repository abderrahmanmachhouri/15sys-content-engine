import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# ─── URLs depuis .env ───
ASYNC_DATABASE_URL = os.getenv("DATABASE_URL")        # postgresql+asyncpg://...
SYNC_DATABASE_URL = os.getenv("SYNC_DATABASE_URL")      # postgresql://...

# ─── ASYNC (pour FastAPI) ───
async_engine = create_async_engine(ASYNC_DATABASE_URL, echo=True)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    """Injection de dépendances pour FastAPI"""
    async with async_session() as session:
        yield session


# ─── SYNC (pour Alembic, scripts, tests) ───
sync_engine = create_engine(SYNC_DATABASE_URL, echo=True)

def get_sync_db():
    """Connexion synchrone pour scripts ou outils"""
    with sync_engine.connect() as conn:
        yield conn