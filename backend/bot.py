from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
from db import add_user
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = str(update.effective_chat.id)
    username = update.effective_user.username or "No username"
    add_user(chat_id, username)

    await update.message.reply_text(f"Hola {username}, tu chat ID es {chat_id}\n Ingresa tus datos en la siguiente URL: http://localhost:5173/")
    print(f"Chat ID: {chat_id}, Username: {username}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()