from shapes.line import Line
from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.quadrilateral import Quadrilateral
from shapes.composite import Composite
import copy


class JsonShapeParser:
    def __init__(self, factory):
        self.factory = factory

    def parse(self, elem):
        shape_type = elem.get("type", "")
        if shape_type == "composite":
            return self._parse_composite(elem)
        elif shape_type in self.factory.composites:
            return copy.deepcopy(self.factory.composites[shape_type])
        else:
            return self._parse_primitive(elem)

    def _parse_composite(self, elem):
        name = elem["name"]
        children = [self.parse(child) for child in elem.get("children", [])]
        composite = Composite(name=name)
        for child in children:
            if child:
                composite.add_shape(child)
        self.factory.composites[name] = composite
        return None

    def _parse_primitive(self, elem):
        shape_type = elem.get("type", "")
        if shape_type == "line":
            return self._parse_line(elem)
        elif shape_type == "circle":
            return self._parse_circle(elem)
        elif shape_type == "triangle":
            return self._parse_triangle(elem)
        elif shape_type == "quadrilateral":
            return self._parse_quadri(elem)
        else:
            raise ValueError(f"No support in shape : {elem}")

    @staticmethod
    def _parse_line(elem):
        points = []
        for point_data in elem.get("children", []):
            points.append((point_data["x"], point_data["y"]))
        return Line(points[0], points[1], elem.get("color"))

    @staticmethod
    def _parse_circle(elem):
        x = int(elem["x"])
        y = int(elem["y"])
        return Circle(
            center=(x, y),
            radius=int(elem["radius"]),
            color_name=elem.get("color"),
            fill_color_name=elem.get("filling_color")
        )

    @staticmethod
    def _parse_triangle(elem):
        points = []
        for point_data in elem.get("children", []):
            points.append((point_data["x"], point_data["y"]))
        return Triangle(points[0], points[1], points[2], elem.get("color"), elem.get("filling_color"))

    @staticmethod
    def _parse_quadri(elem):
        points = []
        for point_data in elem.get("children", []):
            points.append((point_data["x"], point_data["y"]))
        return Quadrilateral(points[0], points[1], points[2], points[3], elem.get("color"), elem.get("filling_color"))
