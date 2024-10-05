# tests/test_memory_game.py

from unittest.mock import patch
from memory_game import generate_sequence, is_list_equal, play


def test_generate_sequence_length():
    difficulty = 5
    sequence = generate_sequence(difficulty)
    assert len(sequence) == difficulty, "Sequence length should match difficulty level."


def test_generate_sequence_range():
    difficulty = 3
    sequence = generate_sequence(difficulty)
    for number in sequence:
        assert 1 <= number <= 101, "Numbers should be between 1 and 101."


def test_is_list_equal_true():
    seq1 = [10, 20, 30]
    seq2 = [10, 20, 30]
    assert is_list_equal(seq1, seq2) == True, "Sequences should be equal."


def test_is_list_equal_false():
    seq1 = [10, 20, 30]
    seq2 = [10, 25, 30]
    assert is_list_equal(seq1, seq2) == False, "Sequences should not be equal."


@patch('memory_game.get_list_from_user')
@patch('memory_game.generate_sequence')
def test_play_win(mock_generate_sequence, mock_get_list_from_user):
    mock_generate_sequence.return_value = [10, 20, 30]
    mock_get_list_from_user.return_value = [10, 20, 30]
    result = play(3)
    assert result == True, "Player should win when sequences match."


@patch('memory_game.get_list_from_user')
@patch('memory_game.generate_sequence')
def test_play_loss(mock_generate_sequence, mock_get_list_from_user):
    mock_generate_sequence.return_value = [10, 20, 30]
    mock_get_list_from_user.return_value = [10, 25, 30]
    result = play(3)
    assert result == False, "Player should lose when sequences do not match."
