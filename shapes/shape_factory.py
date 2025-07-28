from parsers.xml_shape_parser import XmlShapeParser
from parsers.json_shape_parser import JsonShapeParser
from transforms.transform_factory import TransformFactory


class ShapeFactory:

    def __init__(self, extension):
        self.composites = {}
        self.xml_parser = XmlShapeParser(self)
        self.json_parser = JsonShapeParser(self)
        self.extension = extension

    def create_shape_from_element(self, elem):
        if self.extension == 'xml':
            return self.create_shape_from_xml_elem(elem)
        elif self.extension == 'json':
            return self.create_shape_from_json_elem(elem)

    def create_shape_from_xml_elem(self, elem):
        shape = self.xml_parser.parse(elem)
        return self.apply_transform(elem, shape)

    def create_shape_from_json_elem(self, elem):
        shape = self.json_parser.parse(elem)
        return self.apply_transform(elem, shape)

    def apply_transform(self, elem, shape):
        if shape is not None:
            transforms = TransformFactory.create_transforms(elem, self.extension)
            for transform in transforms:
                shape.apply_transform(transform)
        return shape
