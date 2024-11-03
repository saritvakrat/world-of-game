# currency_roulette_game.py

import random

import requests

from games_utils.utils import BAD_RETURN_CODE


def get_exchange_rate():
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        exchange_rate = data['rates']['ILS']
        return exchange_rate
    except Exception as e:
        print(f"An error occurred while fetching exchange rate: {e}")
        return None


def get_money_interval(difficulty, amount):
    exchange_rate = get_exchange_rate()
    if exchange_rate is None:
        return None
    if not (1 <= difficulty <= 5):
        raise ValueError("Difficulty level must be between 1 and 5.")
    if not (1 <= amount <= 100):
        raise ValueError("Amount must be between 1 and 100.")

    total_value = amount * exchange_rate
    margin = 10 - difficulty
    lower_bound = total_value - margin
    upper_bound = total_value + margin
    return lower_bound, upper_bound


def get_guess_from_user(amount):
    while True:
        guess = input(f"Guess the ILS value of {amount} USD: ")
        try:
            return float(guess)
        except ValueError:
            print("Invalid input. Please enter a number.")


def compare_results(difficulty):
    amount = random.randint(1, 100)
    money_interval = get_money_interval(difficulty, amount)
    if money_interval is None:
        print("Unable to fetch exchange rate. Please try again later.")
        return BAD_RETURN_CODE
    lower_bound, upper_bound = money_interval
    guess = get_guess_from_user(amount)
    if lower_bound <= guess <= upper_bound:
        return True
    else:
        return False


def play(difficulty):
    result = compare_results(difficulty)
    if result == BAD_RETURN_CODE:
        return False
    else:
        return result
