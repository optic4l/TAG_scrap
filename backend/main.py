
import requests
import os
from dotenv import load_dotenv
from .scraper import run_scraper
from fastapi import FastAPI
from pydantic import BaseModel
from .db import get_chat_id, add_patente, create_tables
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ en producción mejor poner el dominio de tu frontend
    allow_credentials=True,
    allow_methods=["POST"],  # permite GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)

TOKEN = os.getenv("TELEGRAM_TOKEN")

class ScrapeRequest(BaseModel):
    user_id: int
    patente: str


def telegram_message(message: str, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=data)
    print("Mensaje enviado a Telegram")

@app.post("/scrape/")
def scrape(request: ScrapeRequest):
    add_patente(request.user_id, request.patente)
    result = run_scraper(request.patente)
    print(f"Chat ID obtenido: {request.user_id}")
    if request.user_id:
        telegram_message(result, request.user_id)
        return {"status": "success", "message": "Scraping completed and message sent to Telegram."}
