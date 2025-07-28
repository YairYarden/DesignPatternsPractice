import math
from transforms.base_transform import ITransform


class Rotation(ITransform):
    def __init__(self, angle_degrees: float):
        self.angle_rad = math.radians(angle_degrees)

    def apply(self, points):
        cos_a = math.cos(self.angle_rad)
        sin_a = math.sin(self.angle_rad)
        return [
            (int(float(x) * cos_a - float(y) * sin_a), int(float(x) * sin_a + float(y) * cos_a))
            for x, y in points
        ]
