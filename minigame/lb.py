from kivy.uix.screenmanager import Screen
import kivy.properties as props
import random
import requests

class LeaderboardScreen(Screen):
    lb_info = props.StringProperty()

    def __init__(self, **kwargs):
        super(LeaderboardScreen, self).__init__(**kwargs)
        # will be replaced by real Heroku data
        self.lb_info = str(random.randint(1, 100))

    def get_lb(self):
        """Will make get REST call to heroku app."""
        self.lb_info = str(random.randint(1, 100))

    def update_lb(self, finish_time):
        """Will update leaderboard based on new time"""
        self.get_lb()
        is_new_record = True
        if is_new_record:
            self.enter_initials()

    def enter_initials(self):
        pass