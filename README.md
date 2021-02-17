# Program
My program will be an interactive mobile game where students can learn biology concepts.

### Description of project goal:
My program will be hosted online on Github pages, and will consist of identification minigames (i.e. identifying the parts of a cell, an interactive timed cell cycle game).

### Description of the code:
(It's fine to say you are not sure yet...)
`kivy`: to run the mobile app
`numpy`: to randomly generate locs
Tentative Classes:
- CellPart
- CellLabel
- Leaderboard

### Description of the data:
The data for the leaderboard will be a CSV file stored in the repo, as there will be a set limit of 5 names.

### Description of user interaction:
User can request what game they want to play in the CLI, and then the Kivy window will open.
```
# example command line interface
bio_minigame --cell-id
```
