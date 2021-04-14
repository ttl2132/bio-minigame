import requests
import pandas as pd
import uvicorn
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

@app.post("/scores/{initials}/{score}/{rank}")
def update_scores(initials: str, score: str, rank: int):
    "Checks and updates the leaderboard if a new score is a high score."
    db = get_scores()
    num_ranks = len(db["Time"].keys())
    for i in range(num_ranks-1, num_ranks-rank, -1):
        logger.debug(db.iloc[i])
        db.iloc[i] = db.iloc[i-1]
    db.iloc[rank][0] = initials
    db.iloc[rank][1] = score
    with open(f"{LB_URL}/leaderboard.csv", 'w') as f:
        f.write(db.to_csv())
    return "posted"

@app.get("/scores")
def get_scores():
    "Gets the data from the URL and returns the information as a JSON."
    data = pd.read_csv(f"{LB_URL}/leaderboard.csv")
    data = data.fillna("N/A")
    logger.debug(data)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)