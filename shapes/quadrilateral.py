from shapes.shape import Shape
from shapes.colors import get_color_rgb
import numpy as np
import cv2


class Quadrilateral(Shape):
    def __init__(self, p1, p2, p3, p4, color_name, fill_color_name=None):
        self.p1 = (int(p1[0]), int(p1[1]))
        self.p2 = (int(p2[0]), int(p2[1]))
        self.p3 = (int(p3[0]), int(p3[1]))
        self.p4 = (int(p4[0]), int(p4[1]))
        self.color_rgb = get_color_rgb(color_name)
        if fill_color_name is not None:
            self.fill_color_rgb = get_color_rgb(fill_color_name)
        else:
            self.fill_color_rgb = get_color_rgb("White")

    def get_points(self):
        return [self.p1, self.p2, self.p3, self.p4]

    def set_points(self, points):
        self.p1 = points[0]
        self.p2 = points[1]
        self.p3 = points[2]
        self.p4 = points[3]

    @staticmethod
    def sort_points_clockwise(pts):
        pts = np.array(pts, dtype="float32")

        # Sum and difference of coordinates
        s = pts.sum(axis=1)  # x + y
        diff = np.diff(pts, axis=1)  # x - y

        # Sort corners
        tl = pts[np.argmin(s)]  # smallest sum
        br = pts[np.argmax(s)]  # largest sum
        tr = pts[np.argmin(diff)]  # smallest difference
        bl = pts[np.argmax(diff)]  # largest difference

        return np.array([tl, tr, br, bl], dtype=np.int32)

    def draw(self, canvas):
        pts = self.sort_points_clockwise(np.array([self.p1, self.p2, self.p3, self.p4], dtype=np.int32))
        if self.fill_color_rgb:
            cv2.fillPoly(canvas, [pts], color=self.fill_color_rgb)
        cv2.polylines(canvas, [pts], isClosed=True, color=self.color_rgb, thickness=1)
