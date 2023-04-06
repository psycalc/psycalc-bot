import logging
import os
import json
from dotenv import load_dotenv
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from handlers.start import start
from handlers.handle_response import handle_response
from handlers.next_question import show_next_question

import requests


def download_file_from_github(file_url):
    response = requests.get(file_url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f'Error downloading file: {response.status_code}')


def load_tests_from_json(json_data):
    tests = json.loads(json_data)
    return tests


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")


def load_questions(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


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
    updater.bot_data['questions_list'] = questions_list


    # Add handlers for commands and messages
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(handle_response))
    dispatcher.add_handler(CallbackQueryHandler(
        show_next_question, pattern='next'))

    # Start the bot
    updater.start_polling()

    # Run the bot until Ctrl-C is pressed
    updater.idle()


if __name__ == "__main__":
    main()
