import math
from transforms.base_transform import ITransform


class Rotation(ITransform):
    def __init__(self, angle_degrees: float):
        self.angle_rad = math.radians(angle_degrees)

    def apply(self, points, center_mass):
        cx, cy = center_mass
        cos_a = math.cos(self.angle_rad)
        sin_a = math.sin(self.angle_rad)
        return [
            (int((x-cx) * cos_a - (y-cy) * sin_a) + cx,
             int((x-cx) * sin_a + (y-cy) * cos_a) + cy)
            for x, y in points
        ]
