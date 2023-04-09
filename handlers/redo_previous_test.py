from handlers.next_question import show_next_question
from telegram import Update
from telegram.ext import CallbackContext
def redo_previous_test(update: Update, context: CallbackContext):
    print("redo_previous_test function called")
    query = update.callback_query
    query.answer()

    current_test_index = context.chat_data.get('current_test_index', 0)
    if current_test_index > 0:
        context.chat_data['current_test_index'] = current_test_index - 1

    context.chat_data['current_question_index'] = 0
    show_next_question(update, context)
