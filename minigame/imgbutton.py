from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.app import App
from loguru import logger

class ImageButton(ButtonBehavior, Image):
    """A button image for a cell part."""
    def __init__(self, order, label, source_path, loc, size, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
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
            if self.parent.cur_img == self.parent.last_img:
                logger.debug("Done")
            else:
                self.parent.cur_img += 1
        else:
            logger.debug(f"Incorrect {self.label}")

    def is_current(self):
        """Returns if the cell part matches the current cell part label."""
        return self.order == self.parent.cur_img
