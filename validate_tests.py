import json
import os

def validate_test_format(test_data):
    if not isinstance(test_data, dict):
        print("Invalid format: test data should be a dictionary")
        return False

    required_keys = {"typology", "questions"}
    if not required_keys.issubset(test_data.keys()):
        print(f"Invalid format: test data should contain the following keys: {required_keys}")
        return False

    if not isinstance(test_data["questions"], list):
        print("Invalid format: 'questions' should be a list")
        return False

    for index, question in enumerate(test_data["questions"]):
        if not isinstance(question, dict):
            print(f"Invalid format: question {index + 1} should be a dictionary")
            return False

        question_required_keys = {"title", "options"}
        if not question_required_keys.issubset(question.keys()):
            print(f"Invalid format: question {index + 1} should contain the following keys: {question_required_keys}")
            return False

        if not isinstance(question["options"], list):
            print(f"Invalid format: options for question {index + 1} should be a list")
            return False

    return True

def check_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            test_data = json.load(file)
            if validate_test_format(test_data):
                print(f"Test format is valid for {file_path}")
            else:
                print(f"Test format is not valid for {file_path}")
        except json.JSONDecodeError as error:
            print(f"Error parsing JSON file {file_path}: {error}")

# Define the paths to the JSON files
file_paths = [
    "C:\\Users\\OlegP\\Desktop\\psycalc-bot\\psychosophyQuestions.en.json",
    "C:\\Users\\OlegP\\Desktop\\psycalc-bot\\socionicsQuestions.en.json",
    "C:\\Users\\OlegP\\Desktop\\psycalc-bot\\temporisticsQuestions.en.json",
]

# Check the files
for file_path in file_paths:
    check_file(file_path)
