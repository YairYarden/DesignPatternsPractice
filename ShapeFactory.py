from shapes import Circle, Line


class ShapeFactory:
    shape_map = {
        'Circle': Circle,
        'Line': Line
    }

    @classmethod
    def create_shape(cls, element):
        shape_cls = cls.shape_map.get(element.tag)
        if shape_cls:
            return shape_cls.from_xml(element)
        raise ValueError(f"Unknown shape type: {element.tag}")
