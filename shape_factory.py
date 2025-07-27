from shapes.line import Line
from shapes.circle import Circle


class ShapeFactory:
    shape_map = {
        'Circle': Circle,
        'Line': Line
    }

    @classmethod
    def create_shape(cls, element):
        shape_cls = cls.shape_map.get(element.tag)
        if shape_cls:
            return shape_cls.read_from_xml(element)
        raise ValueError(f"Unknown shape type: {element.tag}")
