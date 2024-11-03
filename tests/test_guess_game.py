# tests/guess_game.py

from unittest.mock import patch

from games.guess_game import generate_number, get_guess_from_user, compare_results, play
from games_utils.utils import BAD_RETURN_CODE


def test_generate_number_range():
    difficulty = 5
    secret_number = generate_number(difficulty)
    assert 0 <= secret_number <= difficulty, "Secret number should be within the difficulty range."


@patch('games.guess_game.input', return_value='3')
def test_get_guess_from_user_valid(mock_input):
    guess = get_guess_from_user(5)
    assert guess == 3, "Guess should be correctly parsed as integer."


@patch('games.guess_game.input', side_effect=['a', '3'])
@patch('games.guess_game.print')
def test_get_guess_from_user_invalid_then_valid(mock_print, mock_input):
    guess = get_guess_from_user(5)
    mock_print.assert_called_with("Invalid input. Please enter a number within the specified range.")
    assert guess == 3, "After invalid input, should accept valid integer."


def test_compare_results_true():
    secret_number = 5
    guess = 5
    assert compare_results(secret_number, guess) == True, "Result should be True when guess matches secret number."


def test_compare_results_false():
    secret_number = 5
    guess = 3
    assert compare_results(secret_number,
                           guess) == False, "Result should be False when guess does not match secret number."


@patch('games.guess_game.get_guess_from_user', return_value=4)
@patch('games.guess_game.generate_number', return_value=4)
def test_play_win(mock_generate_number, mock_get_guess_from_user):
    result = play(5)
    assert result == True, "Player should win when guess matches secret number."


@patch('games.guess_game.get_guess_from_user', return_value=3)
@patch('games.guess_game.generate_number', return_value=4)
def test_play_loss(mock_generate_number, mock_get_guess_from_user):
    result = play(5)
    assert result == False, "Player should lose when guess does not match secret number."


@patch('games.guess_game.get_guess_from_user', return_value=BAD_RETURN_CODE)
@patch('games.guess_game.generate_number', return_value=4)
def test_play_bad_return_code(mock_generate_number, mock_get_guess_from_user):
    result = play(5)
    assert result == False, "Player should lose when BAD_RETURN_CODE is returned."
