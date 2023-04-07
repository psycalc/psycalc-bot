import json
from telegram import Update
from telegram.ext import CallbackContext
from handlers.next_question import show_next_question
from telegram import ParseMode


class UserAnswers:
    def __init__(self):
        self.answers = {}

    def get_chat_data(self, chat_id: int):
        return self.answers.setdefault(chat_id, {"current_question_index": 0})

    def save_answer(self, chat_id: int, question_text: str, selected_answer: str):
        self.answers[chat_id][question_text] = selected_answer

    def increment_question_index(self, chat_id: int):
        self.answers[chat_id]["current_question_index"] += 1


user_answers = UserAnswers()


def handle_response_wrapper(update: Update, context: CallbackContext):
    try:
        query = update.callback_query
        option_number = int(query.data.split("_")[1])
        handle_response(update, context, option_number)
    except Exception as e:
        import traceback
        print("Error occurred:", e)
        traceback.print_exc()

    

def handle_response(update: Update, context: CallbackContext, option_number: int):
    query = update.callback_query
    chat_id = query.message.chat_id

    # Get the current questions list from context.bot_data
    questions_list = context.bot_data.get('questions_list')
    current_test_index = context.chat_data.get('current_test_index')
    if current_test_index is None:
        current_test_index = 0

    questions = questions_list[current_test_index]

    message = query.message


    chat_data = user_answers.get_chat_data(chat_id)
    current_question_index = chat_data["current_question_index"]
    question_text = questions[current_question_index]["title"]
    selected_answer_index = option_number - 1  # Adjust the option_number
    selected_answer = questions[current_question_index]["options"][selected_answer_index]
    user_answers.save_answer(chat_id, question_text, selected_answer)

    # Show next question or result
    if current_question_index + 1 < len(questions):
        # Display next question
        user_answers.increment_question_index(chat_id)
        show_next_question(update, context, current_question_index=current_question_index + 1)
    else:
        # Display result for the current typology
        typology = questions[0].get('typology', 'Unknown Typology')
        result = f"{typology} type:\n\n"
        result += '\n'.join(f"{q['question']}: {user_answers.answers[chat_id][q['question']]}" for q in questions)

        message.reply_text(result, parse_mode=ParseMode.HTML)

        # Clear user answers for the current typology
        for q in questions:
            del user_answers.answers[chat_id][q['question']]

        # Move to the next typology
        if current_test_index + 1 < len(questions_list):
            context.chat_data['current_test_index'] = current_test_index + 1
            context.chat_data['current_question_index'] = 0
            show_next_question(update, context)
        else:
            # No more typologies, clear user answers
            del user_answers.answers[chat_id]