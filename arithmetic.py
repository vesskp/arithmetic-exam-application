import random

tasks = 5
correct = 0
operators = ['+', '-', '*']
level = ""
levels = {
    "1": "simple operations with numbers 2-9",
    "2": "integral squares of 11-29"
}

msg = f"""
Which level do you want? Enter a number:
{"\n".join(f'{key} - {value}' for key, value in levels.items())}
"""

print(msg)
while True:
    level = input()
    if level in ('1', '2'):
        break
    else:
        print('Incorrect format.')


for _ in range(tasks):
    if level == "1":
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        operator = random.choice(operators)
        expression = f'{x} {operator} {y}'
        print(expression)
    else:
        x = random.randint(11, 29)
        expression = f'{x} * {x}'
        print(x)
    while True:
        user_input = input()
        if user_input.strip('-').isnumeric():
            result = eval(expression)
            if user_input == str(result):
                print('Right!')
                correct += 1
            else:
                print('Wrong!')
            break
        else:
            print('Incorrect format.')

print(f'Your mark is {correct}/{tasks}. Would you like to save the result? Enter yes or no.')
ans = input().lower()
if ans == 'yes' or ans == 'y':
    name = input('What is your name? ')
    with open('results.txt', 'a') as file:
        file.write(f'{name}: {correct}/{tasks} in level {level} ({levels[level]})\n')
    print('The results are saved in "results.txt".')
