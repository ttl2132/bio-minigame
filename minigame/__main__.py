"""
Runner for minigame
"""

from .main import MyApp
import argparse

def parse_arguments():
    """
    Parses CLI arguments using argparse
    """

    # init argparse class object
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-g",
        "--gameid",
        help="the game to play"
    )

    parser.add_argument(
        "-i",
        "--initials",
        help="the user's initials"
    )

    # return arg dict-like object containing user arguments
    args = parser.parse_args()
    return args

def run_program():
    "runs the Kivy app"
    args = parse_arguments()
    if not len(args.initials)==3:
        raise Exception("Initials must be 3 characters long.")
    MyApp(args.gameid, args.initials).run()