import math
from foo import utils
def calculate_volume(radius):
    utils.validate_radius(radius)

    foo_volume = (4/3) * math.pi * math.pow(radius, 3)
    return foo_volume
