import kivy

kivy.require('2.0.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout 

Builder.load_file("layouts/main.kv")

# Declare both screens
class MenuScreen(Screen):
    pass

class MenuLayout(GridLayout):
    pass

class SettingsScreen(Screen):
    pass

class MyApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


if __name__ == '__main__':
    MyApp().run()
