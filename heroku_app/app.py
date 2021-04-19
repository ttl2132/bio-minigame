import requests
import pandas as pd
import uvicorn
import psycopg2
import os
from github import Github, InputGitAuthor
from fastapi import FastAPI
from loguru import logger

# create the app as an instance of the fastAPI class
app = FastAPI(debug = True)
LB_URL = "https://raw.githubusercontent.com/ttl2132/ttl2132.github.io/master/data"
HEROKU_URL = "http://bio-minigame.herokuapp.com"

@app.get("/")
def landing_page():
    "Landing page for bio-minigame."
    return "Hi! You can find the leaderboard at this URL/scores"

@app.post("/scores/{game}/{initials}/{score}/{rank}")
def update_scores(game: str, initials: str, score: str, rank: int):
    "Checks and updates the leaderboard if a new score is a high score."
    db = get_scores(game)
    num_ranks = db.shape[0]
    changed_ranks = range(num_ranks-1, rank, -1)
    logger.debug(changed_ranks)
    for i in changed_ranks:
        logger.debug(db.iloc[i])
        db.iloc[i] = db.iloc[i-1]
    db.iloc[rank, 0] = initials
    db.iloc[rank, 1] = score
    push(db.to_csv(index=False))
    logger.debug(f"\n{db.to_csv(index=False)}")
    return db

@app.get("/scores/{game}")
def get_scores(game: str):
    "Gets the data from the URL and returns the information as a JSON."
    db_url = os.getenv('DATABASE_URL')
    con = psycopg2.connect(db_url)
    logger.debug("DB opened")
    db = pd.read_sql(
        f"SELECT * FROM GAMELEADERBOARD WHERE GAME='{game}'",
        con=con
    )
    db = db[db.game==game]
    empty_row = pd.DataFrame([[game, "N/A", 0]], columns=db.columns)
    logger.debug(f"Num rows: {len(db)}")
    logger.debug(f"Empty row: {empty_row}")
    empty_rows = pd.concat(
        [empty_row for i in range(len(db),5)]
        )
    logger.debug(f"Empty Rows: \n{empty_rows}")
    db = pd.concat([db, empty_rows], columns=db.columns).reset_index()
    logger.debug(db)
    return db

def push(content, update=True):
    """From https://towardsdatascience.com/all-the-things-you-can-do-with-github-api-and-python-f01790fca131"""
    token = os.getenv('TOKEN')
    path = "/data/leaderboard.csv"
    g = Github(token)
    repo = g.get_repo("ttl2132/ttl2132.github.io")
    branch = "master"

    message = "Updating github data"
    author = InputGitAuthor(
        "ttl2132",
        "ttl2132@columbia.edu"
    )
    if update:  # If file already exists, update it
        contents = repo.get_contents(path, ref=branch)  # Retrieve old file to get its SHA and path
        repo.update_file(contents.path, message, content, contents.sha, branch=branch, author=author)  # Add, commit and push branch
    else:  # If file doesn't exist, create it
        repo.create_file(path, message, content, branch=branch, author=author)  # Add, commit and push branch

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)