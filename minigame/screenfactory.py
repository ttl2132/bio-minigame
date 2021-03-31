import json
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
            self.imgs = pic_dict["images"]
        logger.debug(len(self.imgs))
        self.load_order = pic_dict["load_order"]
