import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from globals import user_answers
from telegram import ParseMode


def show_next_question(update: Update, context: CallbackContext, current_test_index=None, current_question_index=None):
    if current_test_index is None:
        current_test_index = context.chat_data.get('current_test_index', 0)
    if current_question_index is None:
        current_question_index = context.chat_data.get('current_question_index', 0)
    questions_list = context.bot_data.get('questions_list')

    if current_test_index >= len(questions_list):
        # No more tests
        update.callback_query.edit_message_text(
            text="Sorry, there are no more tests available.")
        return

    questions = questions_list[current_test_index]

    if current_question_index >= len(questions):
        # No more questions in current test
        update.callback_query.edit_message_text(
            text="That's it for this test! Press /start to take another test.")
        return

    question = questions[current_question_index]

    # Save state
    context.chat_data['current_test_index'] = current_test_index
    context.chat_data['current_question_index'] = current_question_index

    # Build message text
    message_text = question["question"] + "\n\n"
    for i, option in enumerate(question["options"]):
        message_text += f"<b>{i}</b>. {option}\n"
    message_text += "\nPlease choose an option by typing /<option_number>."

    # Send message
    update.callback_query.edit_message_text(
        text=message_text, parse_mode=ParseMode.HTML)

