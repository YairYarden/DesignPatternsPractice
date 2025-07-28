from shapes.line import Line
from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.quadrilateral import Quadrilateral
from shapes.composite import Composite
import copy


class ShapeFactory:

    def __init__(self):
        self.composites = {}

    def create_shape_from_xml_elem(self, elem):
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
                shape = self.create_shape_from_xml_elem(child)
                composite.add_shape(shape)
            self.composites[composite.name] = composite
            return None

        elif tag in self.composites:
            shape_instance = copy.deepcopy(self.composites[tag])
            return shape_instance

        else:
            raise ValueError(f"No support in shape : {elem}")

    def create_shape_from_json_elem(self, elem):
        shape_type = elem.get("type", "")
        if shape_type == "composite":
            name = elem["name"]
            children = [self.create_shape_from_json_elem(child) for child in elem.get("children", [])]
            composite = Composite(name=name)
            for child in children:
                if child:
                    composite.add_shape(child)
            self.composites[name] = composite
            return None  # Don't add this to scene directly

        # Handle composite instance reuse (e.g., "type": "Panda")
        elif shape_type in self.composites:
            shape_instance = copy.deepcopy(self.composites[shape_type])  # Implement clone() in Composite
            # self.apply_transform(new_instance, elem)
            return shape_instance

        # Otherwise use shape factory
        else:
            shape = self.create_from_dict(elem)
            return shape


    def create_from_dict(self, data: dict):
        shape_type = data["type"].lower()
        color_name = data.get("color")
        if shape_type == "circle":
            x = int(data["x"])
            y = int(data["y"])
            return Circle(
                center=(x, y),
                radius=int(data["radius"]),
                color_name=data.get("color"),
                fill_color_name=data.get("filling_color")
            )

        elif shape_type == "line":
            points = []
            for point_data in data.get("children", []):
                points.append((point_data["x"], point_data["y"]))
            return Line(points[0], points[1], color_name)

        elif shape_type == "triangle":
            points = []
            for point_data in data.get("children", []):
                points.append((point_data["x"], point_data["y"]))
            return Triangle(points[0], points[1], points[2], color_name, fill_color_name=data.get("filling_color"))

        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
