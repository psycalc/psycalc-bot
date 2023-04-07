import json # library for working with JSON-formatted text strings
import os # library for interacting with the operating system
import requests # library for making HTTP requests
from dotenv import load_dotenv # library for loading environment variables from a .env file

load_dotenv() # Load environment variables from .env file

file_list = ["psychosophyQuestions.en.json", "socionicsQuestions.en.json", "temporisticsQuestions.en.json"] # List of files to check for duplicate questions
api_key = os.getenv("OPENAI_API_KEY") # OpenAI API key
engine = "davinci-codex" # OpenAI API engine to use
endpoint = f"https://api.openai.com/v1/engines/{engine}/completions" # OpenAI API endpoint
prompt = "Rewrite the duplicate question using different words:\n\n" # Prompt to give to OpenAI API

def test_endpoint_and_connection(api_key, endpoint):
    test_response=get_openai_response("Test question", api_key, endpoint, prompt)
    if test_response == "Test question":
        print("OpenAI API connection successful!")
    else:
        raise ValueError("OpenAI API connection failed!")


def get_openai_response(question, api_key, endpoint, prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "prompt": f"{prompt}{question}",
        "max_tokens": 50,
        "temperature": 0.7
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
    response_data = json.loads(response.content)
    if "choices" in response_data:
        return response_data["choices"][0]["text"].strip()
    else:
        raise ValueError(f"Failed to get new question from OpenAI API for question: {question}")
    
def get_test_openai_response(


def get_question_dict(data):
    question_dict = {}
    for question_obj in data:
        question = question_obj["question"]
        if question in question_dict:
            question_dict[question].append(question_obj)
        else:
            question_dict[question] = [question_obj]
    return question_dict


def update_duplicates(duplicates, api_key, endpoint, prompt):
    for question_obj in duplicates:
        question = question_obj["question"]
        new_question = get_openai_response(question, api_key, endpoint, prompt)
        question_obj["question"] = new_question


def update_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def check_duplicate_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        question_dict = get_question_dict(data)
        duplicates = [question_dict[key] for key in question_dict if len(question_dict[key]) > 1]
        if duplicates:
            for dup_list in duplicates:
                for question_obj in dup_list:
                    print(f"Error: Duplicate question found in file {file_path}: {question_obj['question']}")
                update_duplicates(dup_list, api_key, endpoint, prompt)
            update_file(file_path, data)

test_endpoint_and_connection(api_key, endpoint)
for file_path in file_list:
    check_duplicate_questions(file_path)

print("Finished checking for duplicate questions.")
