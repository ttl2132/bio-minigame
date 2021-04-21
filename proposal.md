# Bio Minigame
My program will be an interactive mobile game where students can learn biology concepts.

### Description of project goal:
My program will consist of identification minigames (i.e. identifying the parts of a cell, identifying the parts of the Krebs cycle). The goal of this game is to teach biology concepts in an engaging manner. This is useful to students that may be trying to find the motivation to learn biology.

### User Input
To start the program, the user can provide different options to toggle the game they would like to play, as well as enter their initials for if they get on the leaderboard. Once the game is started, the user may only provide keystrokes or screentouches.

## Description of the code:

### Back End
Imported Packages:
 - `kivy`: to run the mobile app
 - `numpy`: to randomly generate locs and labelling order
 - `fastapi`: to create REST requests in order to do live updates of the leaderboard
 - `uvicorn`: to set up the hosting for the heroku app
 - `psycopg2`: to make calls to the SQL database
 - `requests`: for making REST calls for the Heroku database
 - `pandas`: for organizing the leaderboard information

Classes:
 - MyApp: This includes the screen manager that can toggle between the different screens, as well as the landing page for the app.
 - ScreenFactory(Screen): This creates the screens for each image in the images folder. This is meant to be a parent class for individual games to extend.
 - Leaderboard(GridLayout): This is a database with the leaderboard information hosted on Heroku. It retrieves the information hosted on the site for the scores, and updates them as needed. It will also allow the user to input their initials if they have a record that will be stored in the database.
 - GameScreen(ScreenFactory): This extends the ScreenFactory class, and includes the button behavior based on the cell label. It also contains the prefix for the game required to properly parse the data.
 - Timer: This will create the timer widget that actively updates the time elapsed or resets the timer.
 - ReviewGrid: This contains the review screen material, with all of the images and their corresponding labels.

Function Files:
 - LocGenerator: This is a file that contains functions for generating the locations of the images.

### Front End
Kivy files (with file extension .kv) will be used for styling and binding the functions from the Python files.
Classes:
 - main.kv: Landing page for the game.
 - game.kv: Landing page for the game screen.
 - review.kv: Landing page for the review table.

### Description of the data:
In order to make this library more modular, a standard prefix will be given to each game (i.e. "cellid" and "krebs"). All of the data will be stored with this prefix.

The data for the leaderboard will be a CSV file hosted online on Heroku, with the REST call game parameter being the standard prefix.
- Game char(50)
- Initials char(3): The initials of the record holder.
- Score float: The score of the record holder.

|  Game  | Initials | Time     |
|--------|----------|----------|
| cellid | AAA      | 00:00.00 |
| cellid | BBB      | 00:01.00 |
| cellid | CCC      | 00:02.00 |
| cellid | DDD      | 00:03.00 |
| cellid | EEE      | 00:04.00 |

The data for the game images will stored as a JSON file, stored as a dictionary with the following keys:
- load_order ([str])
- images ({str})
- bounds ({str})

The images dictionary has the following keys:
- source: (str)
- static: (bool)
- bounded: (bool)
- width: (float)
- height: (float)
- location: ({str}) optional

Static means that this image will always stay in the same place on the screen, regardless of if other images are scrambled.
Bounded means that this image is contained within a certain area and is not part of the "main body" of the diagram. For example, the cell wall is not bounded, because the cell parts are stacked on top of it.


The game JSON that will be loaded will be dependent on what game is selected, indicated as a GAME_PREFIX. The images for a game will be placed in a folder with a name mathing the GAME_PREFIX. An example for cellid.json is shown below.

```json
{
  "load_order": ["Cell Wall", "Cell Membrane", "Cytoplasm"],
  "images": {
    "Cell Membrane": {
      "source": "Cell Membrane.png",
      "static": "True",
      "bounded": "False",
      "location": {
        "x": ".15",
        "y": ".05"
      },
      "width": ".7",
      "height": ".6"
    },
    "Nucleus": {
      "source": "Nucleus.png",
      "static": "False",
      "bounded": "True"
    },
    "Vacuole": {
      "source": "Vacuole.png",
      "static": "False",
      "bounded": "True",
      "width": ".2",
      "height": ".4"
    }
  },
  "bounds": {
    "x":".2",
    "y":".1",
    "width": ".6",
    "height": ".5"
  }
}
```

### Description of user interaction:
User can request what game they want to play in the CLI and enter their initials, and then the Kivy window will open.
```
# example command line interface
bio_minigame -g cellid -i TTL
```

### Program Output
The output of this program will be a new Kivy window.

### Similar Programs
The website https://biomanbio.com/ contains similar games explaining biology concepts, but it uses HTML instead of Python. This program will be different, with a smoother interface and gameplay. Furthermore, some of the games are unplayable because they use Adobe Flash, which is no longer supported.

## Overall Plan
1. Get cell memorization game working first.
2. Add cell cycle game to the options.
3. Fix styling for the app.
