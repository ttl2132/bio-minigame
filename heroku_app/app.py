import requests
import pandas as pd
import uvicorn
import psycopg2
import os
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
    logger.debug(f"Rank: {rank}")
    db_url = os.getenv('DATABASE_URL')
    con = psycopg2.connect(db_url)
    cur = con.cursor()
    logger.debug("DB opened")
    cur.execute(
        "INSERT INTO GAMELEADERBOARD (game, initials, time) " +
        f"VALUES ({game},{initials},{score})"
    )
    logger.debug(get_scores(game))
    return get_scores(game)

@app.get("/scores/{game}")
def get_scores(game: str):
    "Gets the data from the URL and returns the information as a JSON."
    db_url = os.getenv('DATABASE_URL')
    con = psycopg2.connect(db_url)
    logger.debug("DB opened")
    q = f"SELECT * FROM GAMELEADERBOARD WHERE GAME='" + game + \
        "' ORDER BY TIME LIMIT 5"
    db = pd.read_sql(q, con=con)
    db = db[db.game==game]
    empty_row = pd.DataFrame([[game, "N/A", 0]], columns=db.columns)
    logger.debug(f"Num rows: {len(db)}")
    logger.debug(f"Empty row: {empty_row}")
    empty_rows = pd.concat(
        [empty_row for i in range(len(db),5)]
        )
    logger.debug(f"Empty Rows: \n{empty_rows}")
    db = pd.concat([db, empty_rows], ignore_index=True).reset_index(drop=True)
    logger.debug(f"Leaderboard DB: \n{db.to_dict()}")
    logger.debug("DB retrieved")
    return db.to_dict()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)