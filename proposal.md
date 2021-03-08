# Bio Minigame
My program will be an interactive mobile game where students can learn biology concepts.

## Interactive Prototype
A rough, interactive prototype of the expected final product is shown [here](https://www.figma.com/proto/7XvpD9wcgbdx1VMqmJGULq/Cell-Memorization?node-id=0%3A3&frame-preset-name=Desktop&scaling=scale-down). Note that the final product will be more randomized and modular than the prototype shown.

### Description of project goal:
My program will consist of identification minigames (i.e. identifying the parts of a cell, identifying the phases of the cell cycle). The goal of this game is to teach biology concepts in an engaging manner. This is useful to students that may be trying to find the motivation to learn biology.

### User Input
To start the program, the user can provide different options to toggle the game they would like to play. Once the game is started, the user may only provide keystrokes or screentouches.

### Description of the code:
 - `kivy`: to run the mobile app
 - `numpy`: to randomly generate locs and labelling order
 - `fastapi`: to create REST requests in order to do live updates of the leaderboard
 - `uvicorn`: to set up the hosting for the heroku app

Tentative Classes:
- Main (includes the different screens available)
- ScreenFactory (creates the screens for each image in the images folder)
- Leaderboard (a SQL database with the leaderboard information hosted on Heroku)
- LocGenerator (a class for generating the locations of the images)
- Cell (includes the changing buttons based on the cell label)

### Description of the data:
In order to make this library more modular, a standard prefix will be given to each game (i.e. "cellid" and "cellcycle"). All of the data will be stored with this prefix.

The data for the leaderboard will be a CSV file hosted online on Heroku, with the REST call game parameter being the standard prefix.
- Initials (str): The initials of the record holder.
- Score (int): The score of the record holder.

| Initials | Time     |
|----------|----------|
| AAA      | 00:00.00 |
| BBB      | 00:01.00 |
| CCC      | 00:02.00 |
| DDD      | 00:03.00 |
| EEE      | 00:04.00 |

The data for the game images will stored as a JSON file, stored as Part_Name (str): File_Path (str). The game JSON that will be loaded will be dependent on what game is selected. The latter two columns represent whether or not that image file is needed for the game. An example for cellid.json is shown below.

```json
{
   "Cell Membrane":"images/Cell Membrane.svg",
   "Cell Wall":"images/Cell Wall.svg",
   "Chloroplast":"images/Chloroplast.svg",
   "Cytoplasm":"images/Cytoplasm.svg",
   "Endoplasmic Reticulum":"images/Endoplasmic Reticulum.svg",
   "Mitochondria":"images/Mitochondria.svg",
   "Nucleus":"images/Nucleus.svg",
   "Vacuole":"images/Vacuole.svg"
}
```

### Description of user interaction:
User can request what game they want to play in the CLI, and then the Kivy window will open.
```
# example command line interface
bio_minigame --cell-id
```

### Program Output
The output of this program will be a new Kivy window.

### Similar Programs
The website https://biomanbio.com/ contains similar games explaining biology concepts, but it uses HTML instead of Python. This program will be different, with a smoother interface and gameplay. Furthermore, some of the games are unplayable because they use Adobe Flash, which is no longer supported.

## TODO
 - Create REST app for the leaderboard
 - Create a timer widget for the app
 - Figure out how to randomly allocate each image without overlap or with depending on if there are layers (i.e. cell wall goes under everything). Includes differentiating static parts, and parts that can be numerous (i.e. a plant cell can have multiple chloroplasts).
 - Figure out how to remove the white backgrounds on some of the images.
