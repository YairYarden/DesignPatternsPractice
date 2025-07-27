from shapes.shape import Shape
import cv2
from shapes.colors import get_color
class Line(Shape):
    def __init__(self, p1, p2, color):
        self.p1 = p1
        self.p2 = p2
        self.color = get_color(color)

    @classmethod
    def read_from_xml(cls, element):
        points = [
            (int(p.attrib['X']), int(p.attrib['Y']))
            for p in element.findall('Point')
        ]
        return cls(p1=points[0], p2=points[1], color=get_color(element.attrib['Color']))

    def draw(self, canvas):
        print(f"Drawing Line with color {self.color} and points {self.p1}, {self.p2}")
        cv2.line(canvas, self.p1, self.p2, self.color, thickness=2)