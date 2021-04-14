import json
from kivy.uix.screenmanager import Screen
import kivy.properties as props
from kivy.app import App
from loguru import logger
from minigame.imgbutton import ImageButton
import numpy as np
import minigame.locgenerator as locgenerator


class ScreenFactory(Screen):
    """Parses the image files to generate the game screen."""
    orders = props.ListProperty([''])
    cur_img = props.NumericProperty()
    last_img = props.NumericProperty()

    def __init__(self, game_name, **kwargs):
        """
        Parameters
        ----------
        game_name (str):
            the name of the game used for file locating
        """
        super(ScreenFactory, self).__init__(**kwargs)
        self.GAME_PREFIX = game_name
        self.imgs = {}
        self.widget_refs = []
        self.orders = ['']
        self.bounds = {}

    def generate_cell(self):
        """Adds the cell parts to the screen."""
        img_locs = locgenerator.generate_picture_layout(
            self.imgs, self.load_order, self.bounds
        )
        order = list(range(len(self.imgs)))
        np.random.shuffle(order)
        label_order = [""] * len(self.imgs)
        for i in range(len(img_locs)):
            count = order[i]
            img_info = img_locs[i]
            image_button = ImageButton(
                count, img_info["label"], img_info["source"], img_info["loc"],
                img_info["size"]
                )
            self.widget_refs.append(image_button)
            self.add_widget(image_button)
            label_order[order[i]] = img_info["label"]
        logger.debug(label_order)
        self.orders = label_order
        self.cur_img = 0
        self.last_img = len(self.orders)-1

    def parse(self):
        """Parses the JSON file to initialize the properties for the game."""
        with open(f"minigame/data/{self.GAME_PREFIX}.json", "r") as f:
            pic_dict = json.load(f)
            self.imgs = pic_dict["images"]
        logger.debug(len(self.imgs))
        self.load_order = pic_dict["load_order"]
        self.bounds = pic_dict["bounds"]

    def on_enter(self):
        """Starts the timer when moved to the game screen."""
        self.time.reset_time()
        self.time.start_time()

    def reset(self):
        """Resets the timer and game with the same layout."""
        self.time.reset_time()
        for button in self.widget_refs:
            self.remove_widget(button)
        self.widget_refs.clear()
        self.generate_cell()
