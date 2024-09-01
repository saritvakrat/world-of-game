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

    choice = get_valid_input("Enter the number of your chosen game: ", 1, len(games))
    difficulty = get_valid_input("Please choose game difficulty from 1 to 5: ", 1, 5)

    return games[choice - 1].split(' - ')[0], difficulty

def get_valid_input(prompt, min_value, max_value):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            value = int(user_input)
            if min_value <= value <= max_value:
                return value
        print(f"Invalid input. Please enter a number between {min_value} and {max_value}.")

def main():
    username = input("Please enter your name: ")
    print(welcome(username))
    game, difficulty = start_play()
    print(f"{username}, you chose to play {game} at difficulty level {difficulty}. May the Odds Be In Your Favor!")

if __name__ == "__main__":
    main()
