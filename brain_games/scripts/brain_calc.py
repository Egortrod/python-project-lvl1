#!/usr/bin/env python3
from random import randint
import prompt


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def welcome_calc():
    print('What is the result of the expression?')


def calc():
    correct_answers = 0
    variants_of_exp = ['*', '-', '+']
    while correct_answers != 3:
        first_number = randint(1, 25)
        second_number = randint(1, 25)
        exp = variants_of_exp[randint(0, 2)]
        print(f'Question: {first_number} {exp} {second_number}')
        user_input = int(input('Your answer: '))
        match exp:
            case '*':
                correct_answer = second_number * first_number
                if correct_answer == user_input:
                    print('Correct!')
                    correct_answers += 1
                else:
                    print(f"'{user_input}' is wrong answer ;(. "
                          f"Correct answer was '{correct_answer}'."
                          f"\nLet's try again, {name}!")
                    break
            case '-':
                correct_answer = first_number - second_number
                if correct_answer == user_input:
                    print('Correct!')
                    correct_answers += 1
                else:
                    print(f"'{user_input}' is wrong answer ;(. "
                          f"Correct answer was '{correct_answer}'."
                          f"\nLet's try again, {name}!")
                    break
            case '+':
                correct_answer = second_number + first_number
                if correct_answer == user_input:
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
    welcome_calc()
    calc()


if __name__ == '__main__':
    main()
