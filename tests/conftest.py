# tests/conftest.py

import pytest
from unittest.mock import patch, mock_open
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def mock_input():
    with patch('builtins.input') as mock:
        yield mock
