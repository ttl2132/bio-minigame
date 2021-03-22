import json
import numpy as np
from kivy.uix.screenmanager import Screen
import kivy.properties as props
from kivy.app import App

class ScreenFactory(Screen):
    orders = props.ListProperty([''])
    """Parses the image files to generate the game screen."""

    def __init__(self, game_name, **kwargs):
        super(ScreenFactory, self).__init__(**kwargs)
        self.GAME_PREFIX = game_name
        self.imgs = {}
        self.order_list = []
        self.orders = ['']

    def parse(self):
        with open(f"minigame/data/{self.GAME_PREFIX}.json", "r") as f:
            pic_dict = json.load(f)
            self.imgs = pic_dict
        self.order_list = list(self.imgs.keys())
        np.random.shuffle(self.order_list)
        self.orders = self.order_list
        print(self.orders)
        App.get_running_app().cur_img = 0
        App.get_running_app().last_img = len(self.orders)
