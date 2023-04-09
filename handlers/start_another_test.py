from handlers.next_question import show_next_question
from telegram import Update
from telegram.ext import CallbackContext
def start_another_test(update: Update, context: CallbackContext):
    print("start_another_test function called")
    query = update.callback_query
    query.answer()

    context.chat_data['current_question_index'] = 0
    show_next_question(update, context)