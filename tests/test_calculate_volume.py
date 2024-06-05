import math
from test_utils import validate_radius
def calculate_volume(radius):
    validate_radius(radius)

    foo_volume = (4/3) * math.pi * math.pow(radius, 3)
    return foo_volume
