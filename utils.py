# utils.py

import os
import time

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    time.sleep(0.5)
    if os.name == 'nt':
        os.system('cls')
    else:
        print("\033[2J\033[H", end='')
