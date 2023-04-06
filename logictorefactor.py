import time

import json

with open('questions.js', 'r', encoding='utf-8') as f:
    question_data = json.load(f)

questions = question_data['questions']
timerInterval = None # store reference to the timer interval so we can stop it

def show_timer():
    global timerInterval
    start = time.time()
    while True:
        now = time.time()
        distance = now - start
        minutes = int(distance // 60)
        seconds = int(distance % 60)
        print("Time: {} minutes {} seconds".format(minutes, seconds))
        time.sleep(1)

def show_question(question):
    # Set up the question UI and display it to the user
    # You can use print statements to display the question and answer choices
    print(f"Вопрос №{questionsCounter + 1} из {len(questions)}\n")
    print(question['text']) # display the question text
    for key, answer in question['answers'].items():
        print(f"{int(key) + 1}. {answer}") # display the answer choices
    while True:
        user_answer = input("Введите свой ответ (1-4): ")
        if user_answer in ['1', '2', '3', '4']:
            break # if the answer is valid, break out of the loop
        print("Неправильный ввод, введите число между 1 и 4.")
    return int(user_answer) - 1 # subtract 1 to get the index of the answer in the answers list since it starts from 0



key_string = 'ploikjuyhgtrfdewsaqzxcvbnm1234567890PLOIKJUYHGTRFDEWSAQZXCVBNM'

def encrypt_number(number, key_string):
    if number < 0 or number > len(key_string):
        print('Ошибка кодирования, слишком большое значение', number)
        return ''
    else:
        return key_string[number]

def decrypt_number(char, key_string):
    return key_string.find(char)

def fn_answer(answer_data):
    # This function cannot be directly translated to Python, as it uses JavaScript-specific syntax and constructs
    pass

def mask_match(mask):
    # This function cannot be directly translated to Python, as it uses JavaScript-specific syntax and constructs
    pass

def show_result():
    # Stop the timer for which the outerInterval variable was necessary
    global timerInterval
    global typesWeights
    global typenames

    sorted_result = []
    for i in range(len(typesWeights)):
        sorted_result.append({'weight': typesWeights[i], 'name': typenames[i]})

    # Sorting the list in descending order based on the 'weight' attribute
    sorted_result.sort(key=lambda x: x['weight'], reverse=True)

    html = '<h3>Результат</h3>'
    html += '<p><b>Вероятний тип: <span>' + sorted_result[0]['name'] + '</span></b></p><div style="font-size: 80%">'
    html += '<p>Набранное количество баллов по типам: (чем больше значение, тем больше шансов, что тип окажется правильным):</p>'

    html += '<ul style="list-style: none">'
    for i in range(len(typesWeights)):
        html += '<li>Тип ' + sorted_result[i]['name'] + ' &mdash; ' + str(round(sorted_result[i]['weight'] * 100) / 100) + '</li>'
    html += '</ul></div>'

    # You can display the result in a UI element or using print statements
    print(html)

def value_encode(value):
    value1 = value // 50
    value2 = value % 50
    return encrypt_number(value1, key_string) + encrypt_number(value2, key_string)

def value_decode(hash, position):
    return decrypt_number(hash[position * 2 + 1], key_string) * 50 + decrypt_number(hash[position * 2 + 2], key_string)

def encode_hash():
    buffer = value_encode(questionsCounter)
    for i in range(len(typesWeights)):
        buffer += value_encode(typesWeights[i] * 30, key_string)
    return buffer

def decodeHash():
    global questionsCounter
    startarray = '' # replace document.location.hash with a string representing the hash value
    hash_len = len(startarray) - 1
    if hash_len == -1 or hash_len != (24 + 1) * 2:
        return False
    questionsCounter = value_decode(startarray, 0)
    for i in range(24):
        typesWeights[i] = value_decode(startarray, i + 1) / 30
    if questionsCounter >= len(questions):
        calculate_result()
        show_result()
        if descriptionElement and descriptionElement.style:
            descriptionElement.style.display = 'none'
        return False
    return True

def hash_change():
    if hash_flag:
        if decodeHash():
            show_question(questions[questionsCounter])

def start_test():
    # Initialize the test and display the first question to the user
    show_question(questions[0])
    show_timer()

def next_question():
    # Process the user's answer to the current question, update the app state accordingly, and display the next question or the result of the test
    pass

def main():
    global questionsCounter
    questionsCounter = 0
    # Initialize the app and start the test
    start_test()

if __name__ == '__main__':
    main()
