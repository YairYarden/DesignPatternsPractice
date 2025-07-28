from shapes.line import Line
from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.quadrilateral import Quadrilateral


class ShapeFactory:
    shape_map = {
        'Circle': Circle,
        'Line': Line,
        'Triangle': Triangle,
        'Quadrilateral': Quadrilateral
    }

    @staticmethod
    def create_shape(elem):
        tag = elem.tag.lower()
        color = elem.attrib.get("Color", "Black")
        points = [
            (int(p.attrib['X']), int(p.attrib['Y']))
            for p in elem.findall('Point')
        ]
        fill_color = elem.attrib.get("FillingColor", "White")

        if tag == "line":
            return Line(points[0], points[1], color)

        elif tag == "circle":
            x = int(elem.attrib['X'])
            y = int(elem.attrib['Y'])
            radius = int(elem.attrib["Radius"])
            shape = Circle((x, y), radius, color, fill_color)

        elif tag == "triangle":
            shape = Triangle(points[0], points[1], points[2], color, fill_color)

        elif tag == "quadrilateral":
            shape = Quadrilateral(points[0], points[1], points[2], points[3], color, fill_color)

        else:
            raise ValueError(f"No support in shape : {elem}")

        return shape
