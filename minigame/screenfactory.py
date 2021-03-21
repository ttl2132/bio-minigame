import json
import numpy as np
from kivy.uix.screenmanager import Screen
import kivy.properties as props

class ScreenFactory(Screen):
    """Parses the image files to generate the game screen."""
    cur_label = props.StringProperty()
    cur_path = props.StringProperty()
    def __init__(self, game_name, **kwargs):
        super(ScreenFactory, self).__init__(**kwargs)
        self.GAME_PREFIX = game_name
        self.imgs = []

    def parse(self):
        with open(f"data/{self.GAME_PREFIX}.json", "r") as f:
            pic_dict = json.load(f)
        self.imgs = list(pic_dict.values())
        self.cur_label = np.random.choice(list(pic_dict.keys()))
        self.cur_path = pic_dict[self.cur_label]
