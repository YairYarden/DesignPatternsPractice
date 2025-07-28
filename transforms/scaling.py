from transforms.base_transform import ITransform


class Scaling(ITransform):
    def __init__(self, sx: float, sy: float):
        self.sx = sx
        self.sy = sy

    def apply(self, points):
        return [int((float(x) * self.sx), int(float(y) * self.sy)) for x, y in points]