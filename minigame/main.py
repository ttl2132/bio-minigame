import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from minigame.cell import CellScreen
from minigame.lb import LeaderboardScreen
import kivy.properties as props

Builder.load_file("minigame/layouts/main.kv")

class MenuScreen(Screen):
    """The main menu screen formatted in layouts/main.kv."""
    pass

class MenuLayout(GridLayout):
    """The layout for the main menu as shown in layouts/main.kv."""
    pass

class MyApp(App):
    """Deploys the app and game information required for tracking the order."""
    cur_img = props.NumericProperty()
    last_img = props.NumericProperty()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(LeaderboardScreen(name='lb'))
        sm.add_widget(CellScreen(name='cellid'))
        return sm


if __name__ == '__main__':
    MyApp().run()
