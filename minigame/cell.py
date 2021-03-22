from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from minigame.screenfactory import ScreenFactory
import minigame.locgenerator as locgenerator
from kivy.app import App
import kivy.properties as props

GAME_PREFIX = "cellid"

class CellScreen(ScreenFactory):

    def __init__(self, **kwargs):
        super(CellScreen, self).__init__(GAME_PREFIX, **kwargs)
        self.parse()
        self.generate_cell()
        self.cur_label = ""
        

    def generate_cell(self):
        img_locs = locgenerator.generate_picture_layout(self.imgs)
        counter = 0
        for label in self.order_list:
            self.add_widget(CellButton(label, counter, img_locs[label]["source"], img_locs[label]["loc"], img_locs[label]["size"]))
            counter += 1
        self.parent

class CellButton(ButtonBehavior, Image):
    """Determines the behavior of a cell part."""
    def __init__(self, order, label, source_path, loc, size, **kwargs):
        super(CellButton, self).__init__(**kwargs)
        self.source = source_path
        self.pos_hint = loc
        self.background_normal = ''
        self.allow_stretch = True
        self.keep_ratio = False
        self.size_hint = size
        self.label = source_path

    def on_press(self):
        if self.is_current():
            print("Correct " + self.label + " " + App.get_running_app().cur_img)
            App.get_running_app().cur_img += 1
            self.toggle_current()
        else:
            print("Incorrect " + self.label)

    def is_current(self):
        return self.order == App.get_running_app().cur_img

    def toggle_current(self):
        self.is_current = not self.is_current