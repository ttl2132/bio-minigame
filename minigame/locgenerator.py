"""A class for determining the locations of each of the images."""
import numpy as np

def generate_picture_layout(imgs):
    """Randomizes the locations of each image."""
    img_locs = {}
    for img in imgs:
        img_locs[img] = {"x": np.random.uniform(0,1), "y": np.random.uniform(0,.67)}
    return img_locs