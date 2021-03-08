from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from screenfactory import ScreenFactory

GAME_PREFIX = "cellid"

class CellScreen(ScreenFactory):
    def __init__(self, **kwargs):
        super(CellScreen, self).__init__(GAME_PREFIX, **kwargs)
        self.parse()

class CellButton(ButtonBehavior, Image):
    """Determines the behavior of a cell part."""
    def __init__(self, **kwargs):
        super(CellButton, self).__init__(**kwargs)
        self.is_current = True

    def on_press(self):
        if self.is_current:
            print("Correct")
            self.toggle_current()
        else:
            print("Incorrect")


    def toggle_current(self):
        self.is_current = not self.is_current