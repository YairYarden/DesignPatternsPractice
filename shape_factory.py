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

    @classmethod
    def create_shape(cls, elem):
        tag = elem.tag.lower()
        color = elem.attrib.get("Color", "Black")
        fill_color = elem.attrib.get("FillingColor", "White")

        if tag == "line":
            points = [
                (int(p.attrib['X']), int(p.attrib['Y']))
                for p in elem.findall('Point')
            ]
            return Line(p1=points[0], p2=points[1], color_name=color)

        elif tag == "circle":
            x = int(elem.attrib["X"])
            y = int(elem.attrib["Y"])
            radius = int(elem.attrib["Radius"])
            shape = Circle((x, y), radius, color, fill_color)

        else:
            raise ValueError(f"No support in shape : {elem}")

        return shape
    