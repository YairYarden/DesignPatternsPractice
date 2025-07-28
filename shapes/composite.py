from shapes.shape import Shape
from transforms.base_transform import ITransform


class Composite(Shape):

    def __init__(self, name=None):
        super().__init__()
        self.name = name
        self.children = []

    # outer list is for different basic shapes, inner list is for different points within a shape
    def get_points(self) -> list[list[tuple[int, int]]]:
        points = []
        for shape in self.children:
            if hasattr(shape, "get_points"):
                points.extend(shape.get_points())
        return points

    def set_points(self, new_points: list[list[tuple[int, int]]]):
        """
                Distribute a flat list of points back to child shapes in order.
                Assumes each child shape knows how many points it needs.
                """
        idx = 0
        for shape in self.children:
            if hasattr(shape, "get_points") and hasattr(shape, "set_points"):
                shape_points = shape.get_points()
                count = len(shape_points)
                shape.set_points(new_points[idx:idx + count])
                idx += count

    def apply_transform(self, transform: ITransform):
        for shape in self.children:
            if hasattr(shape, "apply_transform"):
                shape.apply_transform(transform)

    def add_shape(self, shape):
        self.children.append(shape)

    def draw(self, canvas):
        for shape in self.children:
            shape.draw(canvas)
