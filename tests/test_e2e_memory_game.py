# tests/memory_e2e.py

import os

import pexpect
import pytest


# Full E2E test that fetches the user input and validates the answers
@pytest.mark.skipif(os.name == 'nt', reason="Requires pexpect which is not supported on Windows.")
def test_memory_game_win():
    # Start the application
    # Determine the project root dynamically, assuming this script is located in the tests folder
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    app_path = os.path.join(project_root, 'games_utils', 'app.py')
    child = pexpect.spawn(f'python {app_path}')

    child.expect("Please enter your name: ")
    child.sendline("TestUser")

    child.expect("Please choose a game to play:")
    child.expect("1. Memory Game")
    child.sendline("1")

    child.expect("Please choose game difficulty from 1 to 5: ")
    child.sendline("1")

    child.expect("Memorize the following sequence:")
    child.expect(r"\d+")
    secret_number = child.after.decode().strip()

    child.expect("Please enter the numbers you saw, separated by spaces: ")

    child.sendline(secret_number)

    child.expect("Congratulations! You won!")

    child.terminate()


def test_memory_game_loss():
    # Determine the project root dynamically, assuming this script is located in the tests folder
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    app_path = os.path.join(project_root, 'games_utils', 'app.py')
    child = pexpect.spawn(f'python {app_path}')

    child.expect("Please enter your name: ")
    child.sendline("TestUser")

    child.expect("Please choose a game to play:")
    child.expect("1. Memory Game")
    child.sendline("1")

    child.expect("Please choose game difficulty from 1 to 5: ")
    child.sendline("1")

    child.expect("Memorize the following sequence:")
    child.expect(r"\d+")
    secret_number = child.after.decode().strip()

    child.expect("Please enter the numbers you saw, separated by spaces: ")

    # Send an incorrect number
    wrong_number = str(int(secret_number) + 1) if secret_number.isdigit() else "999"
    child.sendline(wrong_number)

    child.expect("Sorry, you lost. Better luck next time!")

    child.terminate()

