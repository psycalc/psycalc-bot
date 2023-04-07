import os
import json
import logging as logger
from dotenv import load_dotenv
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

from handlers.start import start
from handlers.handle_response import handle_response_wrapper
from handlers.next_question import show_next_question
from telegram import Update
from telegram.ext import CallbackContext

import requests


def download_file_from_github(file_url: str) -> str:
    response = requests.get(file_url)
    if response.status_code == 200:
        return response.text
    raise Exception(f'Error downloading file: {response.status_code}')


def load_tests_from_json(json_data):
    tests = json.loads(json_data)
    return tests


logger.basicConfig(level=logger.INFO,
                   format="%(asctime)s [%(levelname)s] %(message)s")


def handle_user_input(update: Update, context: CallbackContext):
    text = update.message.text
    if text.startswith('/'):
        try:
            option_number = int(text[1:])
            handle_response(update, context, option_number)  # Pass the option_number here
        except ValueError:
            if text == "/skip":
                # -1 indicates skipped question
                handle_response(update, context, -1)
            else:
                update.message.reply_text(
                    "Invalid input. Please type /<option_number> to choose an option or /skip to skip the question.")
    else:
        update.message.reply_text(
            "Please type /<option_number> to choose an option or /skip to skip the question.")

def error_handler(update: Update, context: CallbackContext):
    logger.error(f"Error occurred: {context.error}")
    
    if update and update.message:
        update.message.reply_text("Sorry, something went wrong. Please try again later.")
    elif update and update.callback_query:
        update.callback_query.answer("Sorry, something went wrong. Please try again later.")
    else:
        logger.error("Cannot send a message: update.message and update.callback_query are None")





def main():
    # Load environment variables from .env file
    load_dotenv()

    # Load the Telegram API key from the environment variable
    token = os.getenv("TELEGRAM_API_KEY")

    # Load the list of questions from file
    json_file_urls = [
        'https://raw.githubusercontent.com/psycalc/psycalc-bot/main/psychosophyQuestions.en.json',
        'https://raw.githubusercontent.com/psycalc/psycalc-bot/main/socionicsQuestions.en.json',
        'https://raw.githubusercontent.com/psycalc/psycalc-bot/main/temporisticsQuestions.en.json'
    ]
    questions_list = []
    for url in json_file_urls:
        json_data = download_file_from_github(url)
        questions_list.append(load_tests_from_json(json_data))

    # Set up the bot
    updater = Updater(token=token, use_context=True)

    # Add handlers for commands and messages
    dispatcher = updater.dispatcher
    dispatcher.bot_data['questions_list'] = questions_list
    dispatcher.add_handler(CommandHandler(
        "start", start, pass_args=True, pass_job_queue=True))

    # Pass questions_list to CallbackContext
    dispatcher.add_handler(CallbackQueryHandler(handle_response_wrapper, pattern='^option_'))
    dispatcher.add_handler(CallbackQueryHandler(
        show_next_question, pass_chat_data=True, pass_user_data=True, pass_job_queue=True, pattern='next'))

    # Add handler for user input
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, handle_user_input))
    # Add handler for button callbacks
    # Add error handler to dispatcher
    dispatcher.add_error_handler(error_handler)


    # Start the bot
    updater.start_polling()

    # Run the bot until Ctrl-C is pressed
    updater.idle()


if __name__ == "__main__":
    main()
