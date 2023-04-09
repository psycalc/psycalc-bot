from globals import user_answers
from telegram import Update
from telegram.ext import CallbackContext

from handlers.next_question import show_next_question


def start(update: Update, context: CallbackContext):
    questions_list = context.bot_data.get('questions_list')
    if questions_list is None:
        # If questions_list is not in bot_data, raise an error
        update.message.reply_text("Error: questions list not found. Please contact the bot developer.")
        return

    # Get chat id
    chat_id = update.effective_chat.id

    # Reset user answers if user has already started
    if chat_id in user_answers:
        del user_answers[chat_id]


    # Save questions_list in context.chat_data
    context.chat_data['questions_list'] = questions_list

    update.message.reply_text(
        "Hello! I am a bot that helps you determine your temporistics, psychosophy, and socionics types. Answer the questions so I can help you find out your type.")
    show_next_question(update, context,
                       current_test_index=0, current_question_index=0)
