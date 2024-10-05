# tests/memory_e2e.py

import pytest
import pexpect
import os


# Full E2E test that fetches the user input and validates the answers
@pytest.mark.skipif(os.name == 'nt', reason="Requires pexpect which is not supported on Windows.")
def test_memory_game_win():
    # Start the application
    child = pexpect.spawn('python app.py')

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
    child = pexpect.spawn('python app.py')

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
