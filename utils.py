# utils.py

import os
import time

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1
GAME_RESULTS_FILE = "GameResults.txt"


def screen_cleaner():
    if os.name == 'nt':
        os.system('cls')
    else:
        print("\033[2J\033[H", end='')
