from shapes.shape import Shape
from shapes.colors import get_color_rgb
import cv2
from transforms.base_transform import ITransform

class Circle(Shape):
    def __init__(self, center, radius, color_name, fill_color_name=None):
        self.center = center
        self.radius = radius
        self.color_rgb = get_color_rgb(color_name)
        if fill_color_name is not None:
            self.fill_color_rgb = get_color_rgb(fill_color_name)
        else:
            self.fill_color_rgb = get_color_rgb("White")

    def get_points(self):
        return [self.center]

    def set_points(self, points):
        self.center = points[0]

    def apply_transform(self, transform: ITransform):
        self.set_points(transform.apply(self.get_points()))

    def draw(self, canvas):
        # print(f"Drawing Circle at ({self.x}, {self.y}) with radius {self.radius}")
        # Draw filled circle
        cv2.circle(canvas, self.center, self.radius, self.fill_color_rgb, -1)

        # Draw border
        cv2.circle(canvas, self.center, self.radius, self.color_rgb, 2)
