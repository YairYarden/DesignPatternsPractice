from shapes.shape import Shape
from shapes.colors import get_color_rgb
import cv2

class Circle(Shape):
    def __init__(self, x, y, radius, color_name, fill_color_name=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color_rgb = get_color_rgb(color_name)
        if fill_color_name is not None:
            self.fill_color_rgb = get_color_rgb(fill_color_name)
        else:
            self.fill_color_rgb = get_color_rgb("White")

    @classmethod
    def read_from_xml(cls, element):
        return cls(
            x=int(element.attrib['X']),
            y=int(element.attrib['Y']),
            radius=int(element.attrib['Radius']),
            fill_color_name=element.attrib['FillingColor'],
            color_name=element.attrib['Color']
        )

    def draw(self, canvas):
        print(f"Drawing Circle at ({self.x}, {self.y}) with radius {self.radius}")
        center = (int(self.x), int(self.y))
        # Draw filled circle
        cv2.circle(canvas, center, self.radius, self.fill_color_rgb, -1)

        # Draw border
        cv2.circle(canvas, center, self.radius, self.color_rgb, 2)

