"""A class for determining the locations of each of the images."""
import numpy as np

def generate_picture_layout(imgs):
    """Randomizes the locations of each image."""
    img_locs = {}
    for label in imgs:
        name = imgs[label]
        img_locs[name["source"]] = {}
        if name["static"] == "True":
            img_locs[name["source"]]["loc"] = {key: float(val) for (key,val) in name["location"].items()}
            img_locs[name["source"]]["size"] = (name["width"], name["height"])
        else:
            img_locs[name["source"]]["loc"] = {"x": np.random.uniform(0,1), "y": np.random.uniform(0,.67)}
            img_locs[name["source"]]["size"] =(None,None)
    return img_locs