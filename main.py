from app import welcome, start_play


def main():
    username = input("Please enter your name: ")
    print(welcome(username))
    game, difficulty = start_play()
    print(f"{username} you choose to play game {game} at difficulty level {difficulty}. May the Odds Be In Your Favor")


if __name__ == "__main__":
    main()
