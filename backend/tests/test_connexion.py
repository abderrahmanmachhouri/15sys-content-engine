from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("SYNC_DATABASE_URL")

if not DATABASE_URL:
    print("❌ DATABASE_URL introuvable — vérifie ton fichier .env")
else:
    print(f"🔗 URL chargée : {DATABASE_URL}")
    
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connexion:
            resultat = connexion.execute(text("SELECT version();"))
            version = resultat.fetchone()
            print("✅ Connexion réussie !")
            print("📦 Version PostgreSQL :", version[0])
            
            # Vérifier pgvector
            extensions = connexion.execute(text("SELECT extname FROM pg_extension WHERE extname = 'vector';"))
            ext = extensions.fetchone()
            if ext:
                print("✅ Extension pgvector installée")
            else:
                print("⚠️  Extension pgvector NON installée")
            
            # Lister les tables
            tables = connexion.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"))
            print("📊 Tables existantes :", [row[0] for row in tables])
            
    except Exception as e:
        print("❌ Échec de connexion :", e)






