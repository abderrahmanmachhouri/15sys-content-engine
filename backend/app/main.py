from fastapi import FastAPI
from db.database import get_db

app = FastAPI()

@app.get("/")
def racine():
    return {"message": "Backend  opérationnel"}