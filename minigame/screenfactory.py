import json
import numpy as np
from kivy.uix.screenmanager import Screen
import kivy.properties as props
from kivy.app import App
from loguru import logger

class ScreenFactory(Screen):
    orders = props.ListProperty([''])
    """Parses the image files to generate the game screen."""

    def __init__(self, game_name, **kwargs):
        super(ScreenFactory, self).__init__(**kwargs)
        self.GAME_PREFIX = game_name
        self.imgs = {}
        self.orders = ['']

    def parse(self):
        """Parses the JSON file to initialize the properties for the game."""
        with open(f"minigame/data/{self.GAME_PREFIX}.json", "r") as f:
            pic_dict = json.load(f)
            self.imgs = pic_dict
        self.orders = list(self.imgs.keys())
        np.random.shuffle(self.orders)
        logger.debug(f"Image Order: {self.orders}")
        App.get_running_app().cur_img = 0
        App.get_running_app().last_img = len(self.orders)-1
