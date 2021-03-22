"""A class for determining the locations of each of the images."""
import numpy as np

def generate_picture_layout(imgs):
    """Randomizes the locations of each image."""
    img_locs = {}
    for label in imgs:
        name = imgs[label]
        img_locs[label] = {}
        if name["static"] == "True":
            img_locs[label]["loc"] = {key: float(val) for (key,val) in name["location"].items()}
            img_locs[label]["size"] = (name["width"], name["height"])
            img_locs[label]["source"] = name["source"]
        else:
            img_locs[label]["loc"] = {"x": np.random.uniform(0,1), "y": np.random.uniform(0,.67)}
            img_locs[label]["size"] =(None,None)
            img_locs[label]["source"] = name["source"]
    return img_locs