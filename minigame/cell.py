from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen

class CellScreen(Screen):
    pass

class CellButton(ButtonBehavior, Image):  
    def on_press(self):  
        print ('pressed')
