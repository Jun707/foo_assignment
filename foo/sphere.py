from calculate_volume import calculate_volume

class Sphere:
    def __init__(self, radius):
        self.radius = radius
        
    def volume(self):
        return calculate_volume(self.radius)

