# tests/test_main_score.py

import pytest
from unittest.mock import patch, mock_open
from main_score import app
from utils import SCORES_FILE_NAME, GAME_RESULTS_FILE


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_score_server_no_games(client):
    with patch('main_score.os.path.exists', return_value=False):
        response = client.get('/')
        assert response.status_code == 200
        assert b"No games played yet." in response.data


def test_score_server_with_games(client):
    mock_summaries = [
        "2024-10-04 12:00:00 | Game: Guess Game | Difficulty: 3 | Result: Win\n",
        "2024-10-04 12:05:00 | Game: Memory Game | Difficulty: 2 | Result: Loss\n"
    ]
    mock_score = "18"
    m = mock_open(read_data=mock_score)
    with patch('main_score.os.path.exists') as mock_exists, \
            patch('builtins.open', m):
        # Mock both SCORES_FILE_NAME and GAME_RESULTS_FILE existence
        def side_effect(arg):
            if arg == SCORES_FILE_NAME:
                return True
            elif arg == GAME_RESULTS_FILE:
                return True
            return False

        mock_exists.side_effect = side_effect
        m.return_value.readlines.return_value = mock_summaries
        response = client.get('/')
        assert response.status_code == 200
        assert b"The Score is:" in response.data
        assert b"18" in response.data
        assert b"Game Summaries:" in response.data
        assert b"Guess Game" in response.data
        assert b"Memory Game" in response.data


def test_score_server_read_error(client):
    with patch('main_score.os.path.exists', return_value=True), \
            patch('builtins.open', side_effect=Exception("Read error")):
        response = client.get('/')
        assert response.status_code == 200
        assert b"Error:" in response.data
        assert b"Read error" in response.data
