from shapes.shape import Shape


class Circle(Shape):
    def __init__(self, x, y, radius, fill_color, border_color):
        self.x = x
        self.y = y
        self.radius = radius
        self.fill_color = fill_color
        self.border_color = border_color

    @classmethod
    def from_xml(cls, element):
        return cls(
            x=int(element.attrib['X']),
            y=int(element.attrib['Y']),
            radius=int(element.attrib['Radius']),
            fill_color=element.attrib['FillingColor'],
            border_color=element.attrib['Color']
        )

    def draw(self):
        print(f"Drawing Circle at ({self.x}, {self.y}) with radius {self.radius}")