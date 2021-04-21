from minigame.screenfactory import ScreenFactory
from kivy.app import App
from minigame.timer import Timer
from loguru import logger
import numpy as np


class GameScreen(ScreenFactory):
    """A class for displaying the cell id game screen."""

    time = Timer()

    def __init__(self, game_prefix, **kwargs):
        super(GameScreen, self).__init__(game_prefix, **kwargs)
        self.parse()
        self.generate_game()
