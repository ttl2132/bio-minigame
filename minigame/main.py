from minigame.cell import CellScreen
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
    """Deploys the app and game information required for tracking the order."""
    logger.remove()
    logger.add(
        sys.stderr,
        format="[{level} ] [APP     ] [{time:HH:mm:ss}] {message}",
        level="DEBUG"
    )

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(LeaderboardScreen(name='lb'))
        sm.add_widget(CellScreen(name='cellid'))
        logger.info("Screen manager started")
        return sm


if __name__ == '__main__':
    MyApp().run()
