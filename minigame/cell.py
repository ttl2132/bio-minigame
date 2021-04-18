from minigame.screenfactory import ScreenFactory
from kivy.app import App
from minigame.timer import Timer
from loguru import logger
import numpy as np

GAME_PREFIX = "cellid"


class CellScreen(ScreenFactory):
    """A class for displaying the cell id game screen."""

    time = Timer()

    def __init__(self, **kwargs):
        super(CellScreen, self).__init__(GAME_PREFIX, **kwargs)
        self.parse()
        self.generate_game()
