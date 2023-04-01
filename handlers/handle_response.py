import json
from telegram import Update
from telegram.ext import CallbackContext
from handlers.next_question import show_next_question
from globals import user_answers
from telegram import ParseMode




# Load the list of questions from file
with open("temporisticsQuestions.en.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

def handle_response(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    message = query.message

    # Get saved state
    chat_id = update.callback_query.message.chat_id
    
    # Initialize user_answers if it doesn't exist for the chat_id
    if chat_id not in user_answers:
        user_answers[chat_id] = {}

    current_question_index = user_answers[chat_id].get("current_question_index", 0)
    answers = user_answers[chat_id]

    # Save user answer
    question_text = questions[current_question_index]["question"]
    selected_answer_index = int(data)
    selected_answer = questions[current_question_index]["options"][selected_answer_index]
    answers[question_text] = selected_answer

    # Show next question or result
    if current_question_index + 1 < len(questions):
        # Display next question
        show_next_question(update, context, current_question_index=current_question_index + 1)
    else:
        # Display result
        result = "Psychological type:\n\n"
        for q in questions:
            answer = user_answers[chat_id][q["question"]]
            result += f"{q['question']}: {answer}\n"

        message.reply_text(result, parse_mode=ParseMode.HTML)

        # Clear user answers
        del user_answers[chat_id]
