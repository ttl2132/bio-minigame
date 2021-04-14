from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.app import App
from loguru import logger
from minigame.lb import Leaderboard


class ImageButton(ButtonBehavior, Image):
    """A button image for a cell part."""
    def __init__(self, order, label, source_path, loc, size, **kwargs):
        """
        Parameters
        ----------
        order (int):
            the number that the button is assigned in the question order
        label (str):
            the name of what the image represents
        source_path (str):
            the source path for the image from the images folder
        loc (float, float):
            the location of the image based on image:screen ratio
        size (float, float):
            the size of the image based on image:screen ratio
        """
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
        logger.debug(
            f"{self.label}: {self.height}, {self.width}" +
            f" coords ({self.x},{self.y})"
        )
        if self.is_current():
            logger.debug(f"Correct {self.label}")
            if self.parent.cur_img == self.parent.last_img:
                self.parent.time.stop_time()
                time = self.parent.time.timeText
                logger.debug(f"Done time: {time}")
                lb = Leaderboard(
                    size_hint=(0.3, 0.3), pos_hint=(1.0/3, 1.0/3))
                self.parent.add_widget(lb)
                lb.add_popup_bg()
                self.parent.widget_refs.append(lb)
            else:
                self.parent.cur_img += 1
        else:
            logger.debug(f"Incorrect {self.label}")

    def is_current(self):
        """Returns if the cell part matches the current cell part label."""
        return self.order == self.parent.cur_img
