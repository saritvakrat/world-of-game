# app.py

from guess_game import play as play_guess_game
from currency_roulette_game import play as play_currency_roulette
from memory_game import play as play_memory_game
from score import add_score
from threading import Thread
from main_score import app as flask_app
from utils import screen_cleaner, SCORES_FILE_NAME


def welcome(username):
    return f"Hi {username} and welcome to the World of Games: The Epic Journey"


def clear_score_file():
    """Clears the Scores.txt file by setting the score to zero."""
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write('0')


def start_play():
    games = [
        "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
        "Guess Game - guess a number and see if you chose like the computer.",
        "Currency Roulette - try and guess the value of a random amount of USD in ILS"
    ]

    print("Please choose a game to play:")
    for i, game in enumerate(games, 1):
        print(f"{i}. {game}")

    choice = get_valid_input("Enter the number of your chosen game: ", 1, len(games))
    difficulty = get_valid_input("Please choose game difficulty from 1 to 5: ", 1, 5)

    game_name = games[choice - 1].split(' - ')[0]
    print(f"You chose to play {game_name} at difficulty level {difficulty}. May the Odds Be In Your Favor!")
    screen_cleaner()

    # Start the selected game
    if choice == 1:
        result = play_memory_game(difficulty)
    elif choice == 2:
        result = play_guess_game(difficulty)
    elif choice == 3:
        result = play_currency_roulette(difficulty)
    else:
        print("Invalid choice.")
        return

    # If the user wins, add score
    if result:
        print("Congratulations! You won!")
        add_score(difficulty)
    else:
        print("Sorry, you lost. Better luck next time!")

    # Do not clear the score immediately after the game ends
    # The score will be cleared before starting a new game


def get_valid_input(prompt, min_value, max_value):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Invalid input. Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    def run_flask_app():
        flask_app.run(host='0.0.0.0', port=5000)

    flask_thread = Thread(target=run_flask_app)
    # Do not set daemon=True so the Flask server keeps running
    flask_thread.start()

    username = input("Please enter your name: ")
    print(welcome(username))

    # Clear the score before starting the first game
    clear_score_file()

    while True:
        start_play()
        play_again = input("Do you want to play another game? (y/n): ").lower()
        if play_again != 'y':
            break
        else:
            clear_score_file()

    print("Thank you for playing! The Flask server will keep running to display your score.")
    print("Press Ctrl+C to stop the server and exit.")
    # Keep the main thread alive so the Flask server keeps running
    flask_thread.join()


if __name__ == "__main__":
    main()
