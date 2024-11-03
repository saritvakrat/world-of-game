# tests/test_score.py

import pytest
from unittest.mock import patch, mock_open
from games_utils.score import add_score
from games_utils.utils import SCORES_FILE_NAME


@patch('score.os.path.exists', return_value=True)
@patch('builtins.open', new_callable=mock_open, read_data='10')
def test_add_score_file_exists(mock_file, mock_exists):
    add_score(3)
    # Check read was called
    mock_file.assert_any_call(SCORES_FILE_NAME, 'r')
    # Check write was called with correct new score
    mock_file.assert_any_call(SCORES_FILE_NAME, 'w')
    handle = mock_file()
    handle.write.assert_called_once_with('24')


@patch('score.os.path.exists', return_value=False)
@patch('builtins.open', new_callable=mock_open)
def test_add_score_file_not_exists(mock_file, mock_exists):
    add_score(2)
    # Check write was called with correct new score
    mock_file.assert_any_call(SCORES_FILE_NAME, 'w')
    handle = mock_file()
    handle.write.assert_called_once_with('11')


@patch('score.open', side_effect=IOError("Permission denied"))
def test_add_score_write_error(mock_open_func):
    with patch('builtins.print') as mock_print:
        add_score(3)
        mock_print.assert_called_with("An error occurred while updating the score: Permission denied")


@patch('score.os.path.exists', return_value=True)
@patch('builtins.open', new_callable=mock_open, read_data='invalid')
def test_add_score_invalid_existing_score(mock_file, mock_exists):
    with patch('builtins.print') as mock_print:
        add_score(3)
        mock_print.assert_called_with(
            "An error occurred while updating the score: invalid literal for int() with base 10: 'invalid'")
