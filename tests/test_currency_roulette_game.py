# tests/test_currency_roulette_game.py

import pytest
from unittest.mock import patch
from currency_roulette_game import (
    get_exchange_rate,
    get_money_interval,
    get_guess_from_user,
    compare_results,
    play
)


@patch('currency_roulette_game.requests.get')
def test_get_exchange_rate_success(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {'rates': {'ILS': 3.28}}
    exchange_rate = get_exchange_rate()
    assert exchange_rate == 3.28, "Should return the correct exchange rate."


@patch('currency_roulette_game.requests.get')
def test_get_exchange_rate_failure(mock_get):
    mock_get.side_effect = Exception("API failure")
    exchange_rate = get_exchange_rate()
    assert exchange_rate == None, "Should return None if API call fails."


def test_get_money_interval_valid():
    with patch('currency_roulette_game.get_exchange_rate', return_value=3.28):
        lower, upper = get_money_interval(3, 10)
        total = 10 * 3.28  # 32.8
        margin = 10 - 3  # 7
        assert lower == total - margin  # 25.8
        assert upper == total + margin  # 39.8


def test_get_money_interval_invalid_difficulty():
    with patch('currency_roulette_game.get_exchange_rate', return_value=3.28):
        with pytest.raises(ValueError):
            get_money_interval(6, 10)  # Difficulty > 5


def test_get_money_interval_invalid_amount():
    with patch('currency_roulette_game.get_exchange_rate', return_value=3.28):
        with pytest.raises(ValueError):
            get_money_interval(3, 150)  # Amount > 100


@patch('currency_roulette_game.input', return_value='35.0')
def test_get_guess_from_user_valid(mock_input):
    guess = get_guess_from_user(10)
    assert guess == 35.0, "Guess should be correctly parsed as float."


@patch('currency_roulette_game.input', side_effect=['invalid', '40.0'])
@patch('currency_roulette_game.print')
def test_get_guess_from_user_invalid_then_valid(mock_print, mock_input):
    guess = get_guess_from_user(10)
    mock_print.assert_called_with("Invalid input. Please enter a number.")
    assert guess == 40.0, "After invalid input, should accept valid float."

# Test play function for a win
@patch('currency_roulette_game.get_guess_from_user', return_value=35.0)
@patch('currency_roulette_game.get_money_interval', return_value=(30.0, 40.0))
@patch('currency_roulette_game.print')  # Suppress print during tests
def test_play_win(mock_print, mock_get_money_interval, mock_get_guess_from_user):
    result = play(3)
    assert result == True, "Player should win when guess is within the interval."


# Test play function for a loss
@patch('currency_roulette_game.get_guess_from_user', return_value=45.0)
@patch('currency_roulette_game.get_money_interval', return_value=(30.0, 40.0))
@patch('currency_roulette_game.print')  # Suppress print during tests
def test_play_loss(mock_print, mock_get_money_interval, mock_get_guess_from_user):
    result = play(3)
    assert result == False, "Player should lose when guess is outside the interval."


@patch('currency_roulette_game.get_money_interval', return_value=None)
@patch('currency_roulette_game.print')
def test_play_bad_return_code(mock_print, mock_get_money_interval):
    result = play(3)
    mock_print.assert_called_with("Unable to fetch exchange rate. Please try again later.")
    assert result == False, "Should return False when exchange rate fetch fails."
