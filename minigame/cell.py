from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from screenfactory import ScreenFactory
import locgenerator

GAME_PREFIX = "cellid"

class CellScreen(ScreenFactory):
    def __init__(self, **kwargs):
        super(CellScreen, self).__init__(GAME_PREFIX, **kwargs)
        self.parse()
        self.generate_cell()

    def generate_cell(self):
        img_locs = locgenerator.generate_picture_layout(self.imgs)
        for img in img_locs:
            self.add_widget(CellButton(img, img_locs[img]))
            

class CellButton(ButtonBehavior, Image):
    """Determines the behavior of a cell part."""
    def __init__(self, source_path, loc, **kwargs):
        super(CellButton, self).__init__(**kwargs)
        self.is_current = True
        self.source = source_path
        self.pos_hint = loc
        self.background_normal = ''
        self.size_hint = .5, .5

    def on_press(self):
        if self.is_current:
            print("Correct")
            self.toggle_current()
        else:
            print("Incorrect")


    def toggle_current(self):
        self.is_current = not self.is_current