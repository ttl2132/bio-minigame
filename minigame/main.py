from minigame.gamescreen import GameScreen
from minigame.lb import LeaderboardScreen
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
import kivy.properties as props
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from loguru import logger
import sys
kivy.require('2.0.0')


Builder.load_file("minigame/layouts/main.kv")


class MenuScreen(Screen):
    """The main menu screen formatted in layouts/main.kv."""
    pass


class MenuLayout(GridLayout):
    """The layout for the main menu as shown in layouts/main.kv."""
    pass


class MyApp(App):
    """Deploys the app and adds the required game screens."""
    def __init__(self, gameid, initials, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.GAMEID = gameid
        self.INITIALS = initials

    logger.remove()
    logger.add(
        sys.stderr,
        format="[{level} ] [APP     ] [{time:HH:mm:ss}] {message}",
        level="DEBUG"
    )

    def build(self):
        logger.info(f"{self.GAMEID} game chosen")
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(LeaderboardScreen(name='lb'))
        sm.add_widget(GameScreen(name='game', game_prefix=self.GAMEID))
        logger.info("Screen manager started")
        return sm
