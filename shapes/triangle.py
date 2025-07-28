from shapes.shape import Shape
from shapes.colors import get_color_rgb
import numpy as np
import cv2


class Triangle(Shape):
    def __init__(self, p1, p2, p3, color_name, fill_color_name=None):
        self.p1 = (int(p1[0]), int(p1[1]))
        self.p2 = (int(p2[0]), int(p2[1]))
        self.p3 = (int(p3[0]), int(p3[1]))
        self.color_rgb = get_color_rgb(color_name)
        if fill_color_name is not None:
            self.fill_color_rgb = get_color_rgb(fill_color_name)
        else:
            self.fill_color_rgb = get_color_rgb("White")

    def get_points(self):
        return [self.p1, self.p2, self.p3]

    def set_points(self, points):
        self.p1 = points[0]
        self.p2 = points[1]
        self.p3 = points[2]

    def draw(self, canvas):
        pts = np.array([self.p1, self.p2, self.p3], dtype=np.int32)
        if self.fill_color_rgb:
            cv2.fillPoly(canvas, [pts], color=self.fill_color_rgb)
        cv2.polylines(canvas, [pts], isClosed=True, color=self.color_rgb, thickness=1)
