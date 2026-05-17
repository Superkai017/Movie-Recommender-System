from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')