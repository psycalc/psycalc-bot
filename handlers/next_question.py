import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from globals import user_answers
from telegram import ParseMode


def show_next_question(update: Update, context: CallbackContext, current_test_index=None, current_question_index=None):
    questions_list = context.bot_data.get('questions_list')

    if current_test_index is None:
        current_test_index = context.chat_data.get('current_test_index', 0)
    if current_test_index >= len(questions_list):
        # No more tests
        if update.callback_query:
            update.callback_query.answer()
        else:
            update.message.reply_text(
                text="Sorry, there are no more tests available.")
        return

    questions = questions_list[current_test_index]['questions']
    # Debug output to see the value of 'questions'
    print(f"DEBUG: questions={questions}")

    if current_question_index is None:
        current_question_index = context.chat_data.get('current_question_index', 0)
    if current_question_index >= len(questions):
        # No more questions in current test
        if update.callback_query:
            update.callback_query.answer()
        else:
            update.message.reply_text(
                text="That's it for this test! Press /start to take another test.")
        return

    question = questions[current_question_index]

    # Save state
    context.chat_data['current_test_index'] = current_test_index
    context.chat_data['current_question_index'] = current_question_index

    # Build message text
    message_text = f'<b>Test #{current_test_index + 1}</b>\n' \
                f'<b>Question #{current_question_index + 1}</b>\n' \
                f'{question["title"]}\n\n'

    # Build options as inline keyboard buttons
    keyboard = []
    for i, option in enumerate(question["options"]):
        keyboard.append([InlineKeyboardButton(text=f"{i + 1}. {option}", callback_data=f"option_{i + 1}")])

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Check if the user has clicked the same option before
    user_id = update.effective_user.id
    last_clicked_option = user_answers.get(user_id, {}).get('last_clicked_option')
    current_option = f"option_{current_question_index + 1}"
    if update.callback_query and last_clicked_option == current_option:
        update.callback_query.answer()
        return

    # Save the clicked option
    if not user_answers.get(user_id):
        user_answers[user_id] = {}
    user_answers[user_id]['last_clicked_option'] = current_option

    if update.callback_query:
        update.callback_query.edit_message_text(
            text=message_text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(
            text=message_text, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
