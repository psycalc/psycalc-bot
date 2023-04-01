from globals import user_answers
from telegram import Update
from telegram.ext import CallbackContext

from handlers.next_question import show_next_question

def start(update: Update, context: CallbackContext):
    # Get chat id
    chat_id = update.effective_chat.id

    # Reset user answers if user has already started
    if chat_id in user_answers:
        del user_answers[chat_id]

    update.message.reply_text("Hello! I am a bot that helps you determine your psychological type. Answer the questions so I can help you find out your type.")
    show_next_question(update, context, current_question_index=0)
