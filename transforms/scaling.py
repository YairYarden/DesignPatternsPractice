from transforms.base_transform import ITransform


class Scaling(ITransform):
    def __init__(self, scale_factor: float):
        self.scale_factor = scale_factor

    def apply(self, points):
        return [(int(float(x) * self.scale_factor), int(float(y) * self.scale_factor)) for x, y in points]
