import logging
import os
import json
from dotenv import load_dotenv
from telegram import ParseMode


from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Import the new handlers
from handlers.start import start
from handlers.handle_response import handle_response
from handlers.next_question import show_next_question

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Load environment variables from .env file
load_dotenv()

# Load the Telegram API key from the environment variable
API_KEY = os.environ["TELEGRAM_API_KEY"]

# Load the list of questions from file
with open("temporisticsQuestions.en.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

# Set up the bot
updater = Updater(token=API_KEY, use_context=True)

# Add handlers for commands and messages
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CallbackQueryHandler(handle_response))
updater.dispatcher.add_handler(CallbackQueryHandler(show_next_question, pattern='next'))

# Start the bot
updater.start_polling()

# Run the bot until Ctrl-C is pressed
updater.idle()
