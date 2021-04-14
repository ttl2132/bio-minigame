from kivy.uix.screenmanager import Screen
import kivy.properties as props
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from heroku_app.app import HEROKU_URL
from kivy.graphics import Color, Rectangle
from loguru import logger
import random
import requests
import json


class LeaderboardScreen(Screen):
    """The screen that displays the leaderboard widget."""
    lb_info = props.StringProperty()

    def __init__(self, **kwargs):
        super(LeaderboardScreen, self).__init__(**kwargs)
        self.lb_widget = Leaderboard()

    def on_enter(self):
        """Determines the action"""
        self.lb_widget.update()

class Leaderboard(GridLayout):
    """A widget that contains the initials and times for the leaderboard."""

    def __init__(self, size_hint=None, pos_hint=None, popup=False, **kwargs):
        super(Leaderboard, self).__init__(**kwargs)
        self.label_refs = []
        if size_hint:
            self.size_hint = size_hint
        self.pos_hint={'center_x':.5, 'center_y': .5}
        self.add_widget(Label(text='Initials'))
        self.add_widget(Label(text='Time'))
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
        for old_label in self.label_refs:
            self.remove_widget(old_label)
        lb = self.get_lb()
        num_ranks = len(lb["Initials"].keys())
        for i in range(num_ranks):
            initials_label = Label(text=lb["Initials"][str(i)])
            score_label = Label(text=str(lb["Time"][str(i)]))
            self.label_refs.append(initials_label)
            self.label_refs.append(score_label)
            self.add_widget(initials_label)
            self.add_widget(score_label)
        logger.debug("Leaderboard generated")

    def update(self, finish_time=None):
        """Will update leaderboard based on new time"""
        db_lb = self.get_lb()
        num_ranks = len(db_lb["Initials"].keys())
        if finish_time:
            for i in range(num_ranks):
                if (db_lb["Initials"][str(i)] == "N/A"
                    or finish_time < int(db_lb["Time"][str(i)])):
                    initials = self.enter_initials()
                    requests.post(
                        f"{HEROKU_URL}/scores/{initials}/{finish_time}/{i}"
                        )
        self.generate_leaderboard()

    def get_lb(self):
        """Will make get REST call to heroku app."""
        db_info = requests.get(f"{HEROKU_URL}/scores")
        if db_info.status_code == 200:
            return db_info.json()
        else:
            logger.error(f"{db_info.status_code}: Error returned.")

    def enter_initials(self):
        return "ABC"
        