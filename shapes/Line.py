import Shape


class Line(Shape):
    def __init__(self, color, points):
        self.color = color
        self.points = points

    @classmethod
    def from_xml(cls, element):
        points = [
            (int(p.attrib['X']), int(p.attrib['Y']))
            for p in element.findall('Point')
        ]
        return cls(color=element.attrib['Color'], points=points)

    def draw(self):
        print(f"Drawing Line with color {self.color} and points {self.points}")