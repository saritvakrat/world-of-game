# memory_game.py

import random
import time
from utils import screen_cleaner, BAD_RETURN_CODE


def generate_sequence(difficulty):
    sequence = [random.randint(1, 101) for _ in range(difficulty)]
    return sequence


def get_list_from_user(difficulty):
    while True:
        user_input = input(f"Please enter the numbers you saw, separated by spaces: ")
        try:
            numbers = list(map(int, user_input.strip().split()))
            if len(numbers) != difficulty:
                print(f"You need to enter {difficulty} numbers.")
                continue
            return numbers
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def is_list_equal(sequence, user_sequence):
    return sequence == user_sequence


def play(difficulty):
    sequence = generate_sequence(difficulty)
    print("Memorize the following sequence:")
    print(' '.join(map(str, sequence)))
    time.sleep(0.7)
    screen_cleaner()
    user_sequence = get_list_from_user(difficulty)
    if user_sequence == BAD_RETURN_CODE:
        return False
    return is_list_equal(sequence, user_sequence)
