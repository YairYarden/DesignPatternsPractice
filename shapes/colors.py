COLOR_MAP = {
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255)
}


def get_color(name):
    return COLOR_MAP.get(name, (0, 0, 0))  # default Black
