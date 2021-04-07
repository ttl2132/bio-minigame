"""A class for determining the locations of each of the images."""
import numpy as np
from loguru import logger


def generate_picture_layout(imgs, load_order, bounds):
    """Randomizes the locations of each image."""
    invalid_layout = True
    while invalid_layout:
        invalid_layout = False
        img_locs = []
        coords = []
        # Accounts for images that must be loaded first (canvas images)
        for label in load_order:
            info, bot_left, top_right = get_img_info(imgs, label, bounds)
            img_locs.append(info)
        # Calculates the rest of the images
        for label in imgs:
            if label not in load_order:
                info, bot_left, top_right = get_img_info(imgs, label, bounds)
                img_locs.append(info)
                coords.append((bot_left, top_right))
        logger.debug(f"Img info:\n{img_locs}")
        logger.debug(f"Coordinates Length:\n{len(coords)}")
        logger.debug(f"Coordinates:\n{coords}")
        for i in range(len(coords)):
            for j in range(i+1, len(coords)):
                bl1, tr1 = coords[i]
                bl2, tr2 = coords[j]
                if check_overlap(bl1, tr1, bl2, tr2):
                    logger.debug("Detected overlap")
                    invalid_layout = True
    logger.debug("Returning non-overlapping")
    return img_locs


def get_img_info(imgs, label, bounds):
    name = imgs[label]
    img_info = {"label": label}
    if name["static"] == "True":
        img_info["loc"] = {
            key: float(val) for (key, val) in name["location"].items()
            }
        img_info["size"] = (float(name["width"]), float(name["height"]))
        img_info["source"] = name["source"]
    else:
        if "width" in name.keys():
            img_info["size"] = (float(name["width"]), float(name["height"]))
        else:
            img_info["size"] = (0.1, 0.1)
        img_info["loc"] = get_rand_coords(bounds, name["bounded"],
                                          img_info["size"])
        img_info["source"] = name["source"]
    bot_left = img_info["loc"]
    size = img_info["size"]
    top_right = {
        "x": bot_left["x"] + size[0], "y": bot_left["y"] + size[1]
    }
    return img_info, bot_left, top_right


def get_rand_coords(bounds, bounded, img_size):
    if bounded == "True":
        return {
            "x": np.random.uniform(
                float(bounds["x"]), float(bounds["x"]) +
                float(bounds["width"]) - img_size[0]),
            "y": np.random.uniform(
                float(bounds["y"]), float(bounds["y"]) +
                float(bounds["height"]) - img_size[1])
            }
    else:
        return {"x": np.random.uniform(0, 1), "y": np.random.uniform(0, .67)}

def check_overlap(bl1, tr1, bl2, tr2):
    # If one rectangle is on left side of other
    if (bl1["x"] >= tr2["x"] or tr1["x"] <= bl2["x"]):
        return False
    # If one rectangle is above other
    if (tr1["y"] <= bl2["y"] or tr2["y"] <= bl1["y"]):
        return False
    return True