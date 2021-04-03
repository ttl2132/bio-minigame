"""A class for determining the locations of each of the images."""
import numpy as np
from loguru import logger

def generate_picture_layout(imgs, load_order, bounds):
    """Randomizes the locations of each image."""
    img_locs = []
    # Accounts for images that must be loaded first (canvas images)
    for label in load_order:
        img_locs.append(get_img_info(imgs, label, bounds))
    # Calculates the rest of the images
    for label in imgs:
        if not label in load_order:
            img_locs.append(get_img_info(imgs, label, bounds))
    return img_locs

def get_img_info(imgs, label, bounds):
    name = imgs[label]
    img_info = {"label": label}
    if name["static"] == "True":
        img_info["loc"] = {key: float(val) for (key,val) in name["location"].items()}
        img_info["size"] = (name["width"], name["height"])
        img_info["source"] = name["source"]
    else:
        img_info["loc"] = get_rand_coords(bounds, name["bounded"])
        if "width" in name.keys():
            img_info["size"] = (name["width"], name["height"])
        else:
            img_info["size"] = (None,None)
        img_info["source"] = name["source"]
    return img_info

def get_rand_coords(bounds, bounded):
    if bounded == "True":
        return {"x": np.random.uniform(0,1), "y": np.random.uniform(0,.67)}
    else:
        return {"x": np.random.uniform(0,1), "y": np.random.uniform(0,.67)}