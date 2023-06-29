#!/usr/bin/env python3
from random import randint
import prompt


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def welcome_progression():
    print('What number is missing in the progression?')


def progression_game():
    correct_answers = 0
    while correct_answers != 3:
        first_number = randint(1, 10)
        diff = randint(2, 5)
        result = []
        for idx in range(10):
            result.append(first_number + idx * diff)
        replaced_index = randint(0, 9)
        replaced_number = result[replaced_index]
        result[replaced_index] = '..'
        print('Question:', ' '.join([str(x) for x in result]))
        user_input = int(input('Your answer: '))
        if replaced_number == user_input:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_input}' is wrong answer ;(. "
                  f"Correct answer was '{replaced_number}'."
                  f"\nLet's try again, {name}!")
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


def main():
    welcome()
    welcome_user()
    welcome_progression()
    progression_game()


if __name__ == '__main__':
    main()
