# guess_game.py

import random
from games_utils.utils import BAD_RETURN_CODE


def generate_number(difficulty):
    secret_number = random.randint(0, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        guess = input(f"Guess a number between 0 and {difficulty}: ")
        if guess.isdigit():
            value = int(guess)
            if 0 <= value <= difficulty:
                return value
        print("Invalid input. Please enter a number within the specified range.")


def compare_results(secret_number, guess):
    return secret_number == guess


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    if guess == BAD_RETURN_CODE:
        return False
    return compare_results(secret_number, guess)
