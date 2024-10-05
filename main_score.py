# main_score.py

from flask import Flask
from utils import SCORES_FILE_NAME, GAME_RESULTS_FILE
import os

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read()

        # Read game summaries from GameResults.txt
        if os.path.exists(GAME_RESULTS_FILE):
            with open(GAME_RESULTS_FILE, 'r') as file:
                summaries = file.readlines()
            # Reverse to show the latest games first
            summaries = summaries[::-1]
        else:
            summaries = ["No games played yet.\n"]

        # Generate HTML for game summaries on top of the scores HTML
        summaries_html = ''
        for summary in summaries:
            summaries_html += f"<li>{summary.strip()}</li>"

        html = f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Scores Game</title>
        <style>
            body {{
                background-color: #f0f8ff;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-align: center;
                padding-top: 50px;
            }}
            h1 {{
                color: #333;
            }}
            #score {{
                font-size: 72px;
                color: #4CAF50;
            }}
        </style>
    </head>
    <body>
        <h1>The Score is:</h1>
        <div id="score">{score}</div>
        
         <div id="game-summaries">
            <h2>Game Summaries:</h2>
            <ul>
                {summaries_html}
            </ul>
        </div>
    </body>
</html>"""
        return html

    except Exception as e:
        error_html = f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Scores Game</title>
        <style>
            body {{
                background-color: #ffebee;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-align: center;
                padding-top: 50px;
            }}
            h1 {{
                color: #b71c1c;
            }}
            #score {{
                font-size: 36px;
                color: #d32f2f;
            }}
        </style>
    </head>
    <body>
        <h1>Error:</h1>
        <div id="score" style="color:red">{e}</div>
    </body>
</html>"""
        return error_html
