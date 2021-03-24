### Goal of the project:
The goal for this project is to create a identification bio-mini game. And It is clear to me the goal can be accomplished by using python, `kivy`, `numpy`, `fastapi` and `uvicorn`.
### The data 
It is clear to me the data for this project is image that stored in a json format.
And the data for leaderboard will be stored in the csv format and will be hosted online. 
### The code 
* The current code include a proper skeleton for starting this project. 
* This code so far have data and can identify users' input as correct/incorrect. Also, the code also can update leaderboard and get leaderboard info. 
#### The possible contribution 
I can help creating REST api for the leaderboard. To do so, I created the `app.py` under `/minigame` file. Inside the `app.py`, I wrote the **request** body. So the data can be send to the API from the users.

#### paired-programming2 - lior
I tried to create a timer for the game but struggled with referencing it correctly in the many scripts
as I can't seem to get it to display properly. In general, the timer.py class I created works which can
be seen by uncommenting the print method printing out the seconds to the console. This code is being called from the cell.py file where I create a new Timer() instance and start it. This code should probably be edited so the timer starts when the user presses play as it now starts when the app opens, but I also struggled with implementing this in the main.kv file's on_press. I also added a reference to the timer in cell.py in cellid.kv but for some reason it is not updating. The reference seems to be working because the initial amount can be seen however I am not sure why it is not updating. Still the logic for the timer is there it should just be a matter of referencing it correctly and it should work! Hope this helps and great work so far!
