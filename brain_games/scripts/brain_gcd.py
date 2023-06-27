#!/usr/bin/env python3
from random import randint
import prompt
import math


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def welcome_gcd():
    print('Find the greatest common divisor of given numbers.')


def gcd_game():
    correct_answers = 0
    while correct_answers != 3:
        first_number = randint(1, 100)
        second_number = randint(1, 100)
        correct_answer = math.gcd(first_number, second_number)
        print(f'Question: {first_number} {second_number}')
        user_input = int(input('Your answer: '))
        if user_input == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_input}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            return
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


def main():
    welcome()
    welcome_user()
    welcome_gcd()
    gcd_game()


if __name__ == '__main__':
    main()
