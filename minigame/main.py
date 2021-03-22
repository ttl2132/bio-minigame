import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from minigame.cell import CellScreen
from minigame.lb import LeaderboardScreen

Builder.load_file("minigame/layouts/main.kv")

class MenuScreen(Screen):
    pass

class MenuLayout(GridLayout):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(LeaderboardScreen(name='lb'))
        sm.add_widget(CellScreen(name='cellid'))
        return sm


if __name__ == '__main__':
    MyApp().run()
