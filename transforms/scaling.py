from transforms.base_transform import ITransform


class Scaling(ITransform):
    def __init__(self, scale_factor: float):
        self.scale_factor = scale_factor

    def apply(self, points, center_mass):
        return [(int(x + (self.scale_factor - 1) * (x - center_mass[0])),
                 int(y + (self.scale_factor - 1) * (y - center_mass[1]))) for x, y in points]
