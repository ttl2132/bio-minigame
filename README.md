# Bio Minigame
This program is an interactive game where students can learn biology concepts.

## Short Description:
My project consists of DIY identification minigames (i.e. identifying the parts of a cell) using the Kivy library. The users can play a game and compete against individuals from around the world thanks to a leaderboard hosted on Heroku! The goal of this game is to teach biology concepts in an engaging manner. This is useful to students that may be trying to find the motivation to learn biology.

Something to note is that you can use this program to make your own game, provided you add a .json file format in a similar fashion as cellid.json and kreb.json under the data folder, and the images in a subfolder in the images folder. The name of the folder and .json folder MUST match. This name will also be used to run the program in the terminal.

For more information on how this project is structured, how to set up the JSON, and the libraries the project uses, please check the proposal.md file.

## Installation
Run ```pip install -e .``` ***in the base directory***.
Note: Kivy does not run easily on WSL2. If you would like to play on a Windows machine, I highly suggest you download this repo directly onto Windows and set up a conda environment there instead.

## Game Setup in Terminal
1. Set the variable ```KIVY_NO_ARGS=1``` in your terminal. Note that this may be different based on what OS you are using. On Windows, it is ```set KIVY_NO_ARGS=1```.
2. Run ```bio-minigame -g cellid -i [YOUR_INITIALS]``` ***in the base directory***.
