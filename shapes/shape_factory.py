from shapes.line import Line
from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.quadrilateral import Quadrilateral
from shapes.composite import Composite
import copy


class ShapeFactory:

    def __init__(self):
        self.composites = {}

    def create_shape(self, elem):
        tag = elem.tag
        color = elem.attrib.get("Color", "Black")
        points = [
            (int(p.attrib['X']), int(p.attrib['Y']))
            for p in elem.findall('Point')
        ]
        fill_color = elem.attrib.get("FillingColor", "White")

        if tag == "Line":
            return Line(points[0], points[1], color)

        elif tag == "Circle":
            x = int(elem.attrib['X'])
            y = int(elem.attrib['Y'])
            radius = int(elem.attrib["Radius"])
            return Circle((x, y), radius, color, fill_color)

        elif tag == "Triangle":
            return Triangle(points[0], points[1], points[2], color, fill_color)

        elif tag == "Quadrilateral":
            return Quadrilateral(points[0], points[1], points[2], points[3], color, fill_color)

        elif tag == "Composite":
            composite = Composite(name=elem.attrib.get("Name"))
            if elem.attrib.get("Draw") == "No":
                composite.draw_self = False
            for child in elem:
                shape = self.create_shape(child)
                composite.add_shape(shape)
            self.composites[composite.name] = composite
            return None

        elif tag in self.composites:
            shape_instance = copy.deepcopy(self.composites[tag])
            return shape_instance

        else:
            raise ValueError(f"No support in shape : {elem}")

