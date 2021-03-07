# Bio Minigame
My program will be an interactive mobile game where students can learn biology concepts.

## Interactive Prototype
A rough, interactive prototype of the expected final product is shown [here](https://www.figma.com/proto/7XvpD9wcgbdx1VMqmJGULq/Cell-Memorization?node-id=0%3A3&frame-preset-name=Desktop&scaling=scale-down). Note that the final product will be more randomized and modular than the prototype shown.

### Description of project goal:
My program will consist of identification minigames (i.e. identifying the parts of a cell, an interactive timed cell cycle game). The goal of this game is to teach biology concepts in an engaging manner. This is useful to students that may be trying to find the motivation to learn biology.

### User Input
To start the program, the user can provide different options to toggle the game they would like to play. Once the game is started, the user may only provide keystrokes or screentouches.

### Description of the code:
`kivy`: to run the mobile app

`numpy`: to randomly generate locs

Tentative Classes:
- Main (includes the different screens available)
- ScreenFactory (creates the screens for each image in the images folder)
- Leaderboard (a SQL database with the leaderboard information hosted on Heroku)
- Randomizer (a class for generating the locations of the images)
- Cell (includes the changing buttons based on the cell label)

### Description of the data:
The data for the leaderboard will be a CSV file stored in the repo, as there will be a set limit of 5 names.
- Initials (str): The initials of the record holder.
- Score (int): The score of the record holder.

| Initials | Score | Game_Name |
|----------|-------|-----------|
| AAA      | 100   | Cell_Id   |
| ABC      | 123   | Cell_Cycle|

The data for the game images will also be stored as a CSV file, stored as Part_Name (str), File_Path (str), Cell_Id (bool), Cell_Cycle (bool). The latter two columns represent whether or not that image file is needed for the game.
| Part_Name | File_Path | Cell_Id | Cell_Cycle |
|-----------|-----------|---------|------------|
| AAA       | aaa.svg   | True    | False      |
| ABC       | abc.svg   | False   | True       |

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
