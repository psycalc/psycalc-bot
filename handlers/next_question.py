import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from globals import user_answers
from telegram import ParseMode


def show_next_question(update: Update, context: CallbackContext, current_question_index: int, current_test_index: int):
    # Get chat id
    chat_id = update.effective_chat.id

    # Get the list of questions from context
    questions_list = context.bot_data['questions_list']

    # Get current question
    question = f"{current_question_index+1}. {questions_list[current_test_index][current_question_index]['question']}"

    # Get options for current question
    options = questions_list[current_test_index][current_question_index]["options"]

    # Create answer option buttons
    buttons = [[InlineKeyboardButton(option, callback_data=str(
        index))] for index, option in enumerate(options)]

    # Create markup for buttons
    keyboard = InlineKeyboardMarkup(buttons)

    if update.callback_query:
        if update.callback_query.message.text == question:
            # If the message is not modified, don't attempt to update it
            return

        # If the message is modified, update the message text
        update.callback_query.edit_message_text(text=question, reply_markup=keyboard)
    else:
        # Display question and answer options in chat
        update.message.reply_text(text=question, reply_markup=keyboard)

    # Save the index of the current question for the user
    user_answers.setdefault(chat_id, {})
    user_answers[chat_id]["current_question_index"] = current_question_index
    user_answers[chat_id]["current_test_index"] = current_test_index
