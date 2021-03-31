from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from minigame.screenfactory import ScreenFactory
import minigame.locgenerator as locgenerator
from kivy.app import App
from minigame.timer import Timer
from loguru import logger
import numpy as np

GAME_PREFIX = "cellid"

class CellScreen(ScreenFactory):
    """A class for displaying the cell id game screen."""

    time = Timer()

    def __init__(self, **kwargs):
        super(CellScreen, self).__init__(GAME_PREFIX, **kwargs)
        self.parse()
        self.generate_cell()

    def on_enter(self):
        """Starts the timer when moved to the game screen."""
        self.time.reset_time()
        self.time.start_time()

    def generate_cell(self):
        """Adds the cell parts to the screen."""
        img_locs = locgenerator.generate_picture_layout(self.imgs, self.load_order)
        order = list(range(len(self.imgs)))
        np.random.shuffle(order)
        label_order = [""] * len(self.imgs)
        for i in range(len(img_locs)):
            count = order[i]
            img_info = img_locs[i]
            self.add_widget(CellButton(count, img_info["label"], img_info["source"], img_info["loc"], img_info["size"]))
            label_order[order[i]] = img_info["label"]
        logger.debug(label_order)
        self.orders = label_order
        App.get_running_app().cur_img = 0
        App.get_running_app().last_img = len(self.orders)-1
        self.parent

    def reset(self):
        """Resets the timer and game with the same layout."""
        self.time.reset_time()
        App.get_running_app().cur_img = 0

class CellButton(ButtonBehavior, Image):
    """A button image for a cell part."""
    def __init__(self, order, label, source_path, loc, size, **kwargs):
        super(CellButton, self).__init__(**kwargs)
        self.source = source_path
        self.pos_hint = loc
        self.background_normal = ''
        self.allow_stretch = True
        self.keep_ratio = False
        self.size_hint = size
        self.label = label
        self.order = order

    def on_press(self):
        """Checks if the cell part that was tapped is correct."""
        if self.is_current():
            logger.debug(f"Correct {self.label}")
            if App.get_running_app().cur_img == App.get_running_app().last_img:
                logger.debug("Done")
            else:
                App.get_running_app().cur_img += 1
        else:
            logger.debug(f"Incorrect {self.label}")

    def is_current(self):
        """Returns if the cell part matches the current cell part label."""
        return self.order == App.get_running_app().cur_img
