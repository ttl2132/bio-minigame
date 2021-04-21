from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.app import App
import json


class ReviewScreen(Screen):
    """The screen that displays the leaderboard widget."""

    def __init__(self, **kwargs):
        super(ReviewScreen, self).__init__(**kwargs)


class ReviewGrid(GridLayout):
    """A container for the table that will show the review images."""

    def __init__(self, **kwargs):
        super(ReviewGrid, self).__init__(**kwargs)
        GAME_PREFIX = App.get_running_app().GAMEID
        with open(f"minigame/data/{GAME_PREFIX}.json", "r") as f:
            pic_dict = json.load(f)
            for img in pic_dict["images"]:
                file_name = pic_dict['images'][img]['source']
                src = f"minigame/images/{GAME_PREFIX}/{file_name}"
                self.add_widget(Label(text=img, font_size='20sp'))
                self.add_widget(Image(source=src, keep_ratio=True))