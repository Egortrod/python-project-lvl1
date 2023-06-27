#!/usr/bin/env python3
from random import randint
import prompt


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def welcome_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime_game():
    correct_answers = 0
    while correct_answers != 3:
        question = randint(1, 50)
        correct_answer = 'yes'
        print(f'Question: {question}')
        for i in range(2, (question // 2) + 1):
            if question % i == 0:
                correct_answer = 'no'
                break
        user_input = str(input('Your answer: '))
        if user_input == correct_answer:
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
    welcome_prime()
    prime_game()


if __name__ == '__main__':
    main()
