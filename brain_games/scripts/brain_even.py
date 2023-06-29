#!/usr/bin/env python3
from random import randint
# from brain_games.cli import welcome_user
import prompt


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def welcome_even_or_not():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def even_or_not_game():
    correct_answers = 0
    while correct_answers != 3:
        question = randint(1, 100)
        if question % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {question}')
        user_input = input('Your answer: ')
        if (user_input == 'yes' and question % 2 == 0) or (
            user_input == 'no' and question % 2 == 1
        ):
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_input}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


def main():
    welcome()
    welcome_user()
    welcome_even_or_not()
    even_or_not_game()


if __name__ == '__main__':
    main()
