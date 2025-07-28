from transforms.base_transform import ITransform


class TranslationX(ITransform):
    def __init__(self, dx):
        self.dx = dx

    def apply(self, points):
        return [(int(x + self.dx), y) for x, y in points]


class TranslationY(ITransform):
    def __init__(self, dy):
        self.dy = dy

    def apply(self, points):
        return [(x, int(y + self.dy)) for x, y in points]