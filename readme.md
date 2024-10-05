# World of Games: The Epic Journey

Welcome to the **World of Games: The Epic Journey**! This Python application offers a collection of mini-games designed to challenge and entertain. Users can select a game, set a difficulty level, and track their scores over time.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Games Included](#games-included)
- [Score Management](#score-management)
- [Requirements](#requirements)

## Overview

**World of Games** is a console-based Python application featuring three interactive games:

1. **Memory Game**: Test your memory by recalling a sequence of numbers displayed briefly.
2. **Guess Game**: Try to guess a randomly generated number within a specified range.
3. **Currency Roulette**: Guess the equivalent value of a random amount of USD in ILS based on current exchange rates.

The application also includes a scoring system that accumulates points based on your performance and a Flask-based server to display your total score via a web browser.

## Project Structure

```
world-of-game/
├── tests/                      # folder with all tests files
├── .github/workflows           # folder with github workflows
├── app.py                      # Main application logic
├── main.py                     # Entry point to start the game
├── utils.py                    # Utility functions and shared variables
├── score.py                    # Score management functions
├── main_score.py               # Flask server to display the score
├── guess_game.py               # Guess Game implementation
├── currency_roulette_game.py   # Currency Roulette Game implementation
├── memory_game.py              # Memory Game implementation
├── Scores.txt                  # File storing the user's score
├── GameResutls.txt             # File storing the user's scores between games
└── README.md                   # Project documentation
```

## Installation

1. **Clone the Repository**:

   ```bash
   git clone hgit@github.com:saritvakrat/world-of-game.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd world-of-game
   ```

3. **Create a Virtual Environment (Optional but Recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows use `venv\Scripts\activate`
   ```

4. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Game Application

To start the game application, run:

```bash
python main.py
```

Navigate to [http://localhost:5000/](http://localhost:5000/) in your web browser to view your score.

### Playing the Games

1. **Follow the Prompts**:
   - **Enter Your Name**: When prompted, input your name.
   - **Select a Game**: Choose a game to play by entering the corresponding number:
      - `1`: Memory Game
      - `2`: Guess Game
      - `3`: Currency Roulette
   - **Set Difficulty Level**: Choose a difficulty level from `1` (Easy) to `5` (Hard).

2. **Game Instructions**: Each game will provide specific instructions on how to play.

3. **Viewing Your Score**:
   - After each game, your score will be updated in `Scores.txt`.
   - Use the score server to view your accumulated score.

## Games Included

### 1. Memory Game (`memory_game.py`)

- **Objective**: Memorize a sequence of random numbers displayed for a short duration and then recall them.
- **How to Play**:
   - A sequence of numbers will appear on the screen for `0.7` seconds.
   - After the screen is cleared, you will be prompted to input the numbers you remember.
   - Win by correctly recalling the entire sequence.

### 2. Guess Game (`guess_game.py`)

- **Objective**: Guess a randomly generated number within a specified range based on the chosen difficulty.
- **How to Play**:
   - The computer generates a secret number between `1` and the selected difficulty level.
   - You are prompted to guess the number.
   - Win by correctly guessing the secret number.

### 3. Currency Roulette (`currency_roulette_game.py`)

- **Objective**: Guess the value of a random amount of USD in ILS within an acceptable range based on the difficulty level.
- **How to Play**:
   - A random USD amount between `1` and `100` is generated.
   - You are asked to guess the equivalent amount in ILS.
   - The acceptable range is calculated as `±(10 - difficulty)` ILS.
   - Win by guessing within the acceptable range.

## Score Management

- **Scoring System**:
   - Points are awarded based on the formula: `POINTS_OF_WINNING = (DIFFICULTY X 3) + 5`.
   - Your total score is accumulated in the `Scores.txt` file.
- **Viewing the Score**:
   - Run the `main_score.py` server.
   - Access [http://localhost:5000/](http://localhost:5000/) to view your current score in an HTML page.

## Requirements

- **Python**: 3.8.x or higher
- **Packages**:
   - `Flask`: For running the score server.
- **Operating System**: Cross-platform (Windows, macOS, Linux)

## Unit tests
Unit tests are under /tests folder, to run unit tests run `pytest`

---

**Enjoy your journey in the World of Games! May the odds be ever in your favor.**

---

