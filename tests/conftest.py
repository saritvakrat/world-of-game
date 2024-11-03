# tests/conftest.py

import os
import sys
from unittest.mock import patch

import pytest

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def mock_input():
    with patch('builtins.input') as mock:
        yield mock
