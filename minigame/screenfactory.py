import json
import numpy as np
from kivy.uix.screenmanager import Screen

class ScreenFactory(Screen):
    def __init__(self, game_name, **kwargs):
        super(ScreenFactory, self).__init__(**kwargs)
        self.GAME_PREFIX = game_name
        self.parse()

    def parse(self):
        with open(f"data/{self.GAME_PREFIX}.json", "r") as f:
            pic_dict = json.load(f)
        self.cur_label = np.random.choice(list(pic_dict.keys()))
        self.cur_path = pic_dict[self.cur_label]