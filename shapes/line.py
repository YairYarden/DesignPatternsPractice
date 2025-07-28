from shapes.shape import Shape
import cv2
from shapes.colors import get_color_rgb
class Line(Shape):
    def __init__(self, p1, p2, color_name):
        self.p1 = p1
        self.p2 = p2
        self.color_rgb = get_color_rgb(color_name)

    def get_points(self):
        return [self.p1, self.p2]

    def set_points(self, points):
        self.p1 = points[0]
        self.p2 = points[1]

    def draw(self, canvas):
        # print(f"Drawing Line with color {self.color_rgb} and points {self.p1}, {self.p2}")
        cv2.line(canvas, self.p1, self.p2, self.color_rgb, thickness=2)