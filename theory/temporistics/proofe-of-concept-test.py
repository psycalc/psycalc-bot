from tempo_questions import questions

results = {
    'Минуле': [0, 0, 0, 0],
    'Майбутнє': [0, 0, 0, 0],
    'Вічність': [0, 0, 0, 0],
    'Теперішнє': [0, 0, 0, 0],
}

possible_answers = ['1', '2', '3', '4', '5']

for time, time_questions in questions.items():
    print(f'\n{time}:\n')
    for i, position_questions in enumerate(time_questions):
        for j, question in enumerate(position_questions):
            print(f"{j + 1}) {question}")
        while True:
            answer = input(f'Виберіть відповідь (1-5): ')
            if answer in possible_answers:
                results[time][i] += int(answer)
                break
            else:
                print("Будь ласка, введіть число від 1 до 5.")

print('\nРезультати:')
for time, time_results in results.items():
    print(f'{time}: {time_results}')

max_positions = [0, 0, 0, 0]
for time, time_results in results.items():
    for i, value in enumerate(time_results):
        if value > max_positions[i]:
            max_positions[i] = value

print('\nНайбільш виражені позиції для кожного часу:')
for i, max_position in enumerate(max_positions):
    print(f'Позиція {i + 1}: {max_position}')
