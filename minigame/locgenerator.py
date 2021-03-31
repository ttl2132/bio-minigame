"""A class for determining the locations of each of the images."""
import numpy as np
from loguru import logger

def generate_picture_layout(imgs, load_order):
    """Randomizes the locations of each image."""
    img_locs = []
    for label in load_order:
        name = imgs[label]
        img_info = {"label": label}
        if name["static"] == "True":
            img_info["loc"] = {key: float(val) for (key,val) in name["location"].items()}
            img_info["size"] = (name["width"], name["height"])
            img_info["source"] = name["source"]
        else:
            img_info["loc"] = {"x": np.random.uniform(0,1), "y": np.random.uniform(0,.67)}
            img_info["size"] =(None,None)
            img_info["source"] = name["source"]
        img_locs.append(img_info)
    for label in imgs:
        if not label in load_order:
            name = imgs[label]
            img_info = {"label": label}
            if name["static"] == "True":
                img_info["loc"] = {key: float(val) for (key,val) in name["location"].items()}
                img_info["size"] = (name["width"], name["height"])
                img_info["source"] = name["source"]
            else:
                img_info["loc"] = {"x": np.random.uniform(0,1), "y": np.random.uniform(0,.67)}
                img_info["size"] =(None,None)
                img_info["source"] = name["source"]
            img_locs.append(img_info)
    return img_locs