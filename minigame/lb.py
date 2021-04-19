from kivy.uix.screenmanager import Screen
import kivy.properties as props
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from heroku_app.app import HEROKU_URL
from kivy.graphics import Color, Rectangle
from loguru import logger
import random
import requests
import pandas as pd
from kivy.app import App


class LeaderboardScreen(Screen):
    """The screen that displays the leaderboard widget."""
    lb_info = props.StringProperty()

    def __init__(self, **kwargs):
        super(LeaderboardScreen, self).__init__(**kwargs)
        self.lb_widget = Leaderboard()

    def on_enter(self):
        """Determines the action"""
        self.remove_widget(self.lb_widget)
        self.lb_widget = Leaderboard()

class Leaderboard(GridLayout):
    """A widget that contains the initials and times for the leaderboard."""

    def __init__(self, size_hint=None, pos_hint=None, popup=False, **kwargs):
        super(Leaderboard, self).__init__(**kwargs)
        self.label_refs = []
        if size_hint:
            self.size_hint = size_hint
        if popup:
            self.add_popup_bg()
        self.pos_hint={'center_x':.5, 'center_y': .5}
        self.add_widget(Label(text='Initials'))
        self.add_widget(Label(text='Time'))
        self.game = App.get_running_app().GAMEID
        self.generate_leaderboard()
        self.bg = None
        self.cols = 2

    def add_popup_bg(self):
        with self.canvas.before:
            Color(0, 0, 0)
            self.bg = Rectangle(
                pos=(300, 100),
                height = self.parent.height,
                size=self.parent.size
                )
            self.bind(pos=self.update_bg, size=self.update_bg)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def generate_leaderboard(self):
        """Used for created the widgets to display in the grid layout"""
        self.clear_widgets()
        updated_lb=self.get_lb()
        logger.debug(updated_lb)
        updated_lb=pd.DataFrame.from_dict(updated_lb)
        num_ranks = updated_lb.shape[0]
        for i in range(num_ranks):
            initials_label = Label(text=updated_lb["initials"][str(i)])
            rounded_time = "{:.2f}".format(updated_lb["time"][str(i)])
            score_label = Label(text=rounded_time)
            self.label_refs.append(initials_label)
            self.label_refs.append(score_label)
            self.add_widget(initials_label)
            self.add_widget(score_label)
        logger.debug("Leaderboard generated")

    def update(self, time=None):
        """Will update leaderboard based on new time"""
        db_lb = self.get_lb()
        num_ranks = len(db_lb)
        updated = False
        if time:
            for i in range(num_ranks):
                if (db_lb["initials"][str(i)] == "N/A"
                    or time < int(db_lb["time"][str(i)])):
                    name = App.get_running_app().INITIALS
                    logger.debug(f"Name: {name}")
                    lb = requests.post(
                    f"{HEROKU_URL}/scores/{self.game}/{name}/{time}/{i}"
                    )
                    logger.debug(lb)
                    updated = True
                    break
            self.generate_leaderboard()
        if not updated:
            self.generate_leaderboard()

    def get_lb(self):
        """Will make get REST call to heroku app."""
        db_info = requests.get(f"{HEROKU_URL}/scores/{self.game}")
        if db_info.status_code == 200:
            return pd.DataFrame.from_dict(db_info.json())
        else:
            logger.error(f"{db_info.status_code}: Error returned.")
