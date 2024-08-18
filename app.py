def welcome(username):
    return f"Hi {username} and welcome to the World of Games: The Epic Journey"


def start_play():
    games = [
        "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
        "Guess Game - guess a number and see if you chose like the computer.",
        "Currency Roulette - try and guess the value of a random amount of USD in ILS"
    ]

    print("Please choose a game to play:")
    for i, game in enumerate(games, 1):
        print(f"{i}. {game}")

    while True:
        try:
            choice = int(input("Enter the number of your chosen game: "))
            if 1 <= choice <= len(games):
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Invalid difficulty. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return games[choice - 1].split(' - ')[0], difficulty
