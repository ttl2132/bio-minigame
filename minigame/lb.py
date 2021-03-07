from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as props
from kivy.uix.gridlayout import GridLayout
import random

class LeaderboardScreen(Screen):
    lb_info = props.StringProperty()

    def __init__(self, **kwargs):
        super(LeaderboardScreen, self).__init__(**kwargs)
        self.lb_info = str(random.randint(1, 100))

    def update(self):
        """Will make REST call to heroku app."""
        self.lb_info = str(random.randint(1, 100))
