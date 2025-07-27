from shapes.shape import Shape
from shapes.colors import get_color
import cv2

class Circle(Shape):
    def __init__(self, x, y, radius, fill_color, border_color):
        self.x = x
        self.y = y
        self.radius = radius
        self.fill_color = get_color(fill_color)
        self.border_color = get_color(border_color)

    @classmethod
    def read_from_xml(cls, element):
        return cls(
            x=int(element.attrib['X']),
            y=int(element.attrib['Y']),
            radius=int(element.attrib['Radius']),
            fill_color=element.attrib['FillingColor'],
            border_color=element.attrib['Color']
        )

    def draw(self, canvas):
        print(f"Drawing Circle at ({self.x}, {self.y}) with radius {self.radius}")
        center = (int(self.x), int(self.y))
        # Draw filled circle
        cv2.circle(canvas, center, self.radius, self.fill_color, -1)
        # Draw border
        cv2.circle(canvas, center, self.radius, self.border_color, 2)