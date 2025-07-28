from shapes.line import Line
from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.quadrilateral import Quadrilateral
from shapes.composite import Composite
import copy


class XmlShapeParser:
    def __init__(self, factory):
        self.factory = factory

    def parse(self, elem):
        tag = elem.tag
        if tag == "Composite":
            return self._parse_composite(elem)
        elif tag in self.factory.composites:
            return copy.deepcopy(self.factory.composites[tag])
        else:
            return self._parse_primitive(elem)

    def _parse_composite(self, elem):
        composite = Composite(name=elem.attrib.get("Name"))
        for child in elem:
            shape = self.parse(child)
            if shape:
                composite.add_shape(shape)
        self.factory.composites[composite.name] = composite
        return None

    def _parse_primitive(self, elem):
        tag = elem.tag
        if tag == "Line":
            return self._parse_line(elem)
        elif tag == "Circle":
            return self._parse_circle(elem)
        elif tag == "Triangle":
            return self._parse_triangle(elem)
        elif tag == "Quadrilateral":
            return self._parse_quadri(elem)
        else:
            raise ValueError(f"No support in shape : {elem}")

    @staticmethod
    def _parse_line(elem):
        points = [
            (int(p.attrib['X']), int(p.attrib['Y']))
            for p in elem.findall('Point')
        ]
        color = elem.attrib.get("Color", "Black")
        return Line(points[0], points[1], color)

    @staticmethod
    def _parse_circle(elem):
        x = int(elem.attrib['X'])
        y = int(elem.attrib['Y'])
        radius = int(elem.attrib["Radius"])
        color = elem.attrib.get("Color", "Black")
        fill_color = elem.attrib.get("FillingColor", "White")
        return Circle((x, y), radius, color, fill_color)

    @staticmethod
    def _parse_triangle(elem):
        points = [
            (int(p.attrib['X']), int(p.attrib['Y']))
            for p in elem.findall('Point')
        ]
        color = elem.attrib.get("Color", "Black")
        fill_color = elem.attrib.get("FillingColor", "White")
        return Triangle(points[0], points[1], points[2], color, fill_color)

    @staticmethod
    def _parse_quadri(elem):
        points = [
            (int(p.attrib['X']), int(p.attrib['Y']))
            for p in elem.findall('Point')
        ]
        color = elem.attrib.get("Color", "Black")
        fill_color = elem.attrib.get("FillingColor", "White")
        return Quadrilateral(points[0], points[1], points[2], points[3], color, fill_color)