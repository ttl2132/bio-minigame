from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.graphics.svg import Svg
import kivy.properties as props
import json
import numpy as np

GAME_PREFIX = "cellid"

class CellScreen(Screen):
    cur_label = props.StringProperty()
    cur_path = props.StringProperty()

    def __init__(self, **kwargs):
        super(CellScreen, self).__init__(**kwargs)
        self.parse()

    def parse(self):
        with open(f"data/{GAME_PREFIX}.json", "r") as f:
            df = json.load(f)
        self.cur_label = np.random.choice(list(df.keys()))
        self.cur_path = "images/Cytoplasm.png"


class CellButton(ButtonBehavior, Image):

    def __init__(self, **kwargs):
        super(CellButton, self).__init__(**kwargs)
        self.is_current = True

    def on_press(self):
        if self.is_current:
            print("Correct")
            self.toggle_current()
        else:
            print("Incorrect")


    def toggle_current(self):
        self.is_current = not self.is_current