"""A class for determining the locations of each of the images."""
import numpy as np

def generate_picture_layout(imgs):
    """Randomizes the locations of each image."""
    img_locs = {}
    for label in imgs:
        name = imgs[label]
        if name["static"] == "True":
            img_locs[name["source"]] = {key: float(val) for (key,val) in name["location"].items()}
        else:
            img_locs[name["source"]] = {"x": np.random.uniform(0,1), "y": np.random.uniform(0,.67)}
    return img_locs