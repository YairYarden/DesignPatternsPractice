from parsers.xml_shape_parser import XmlShapeParser
from parsers.json_shape_parser import JsonShapeParser
from transforms.transform_factory import TransformFactory


class ShapeFactory:

    def __init__(self):
        self.composites = {}
        self.xml_parser = XmlShapeParser(self)
        self.json_parser = JsonShapeParser(self)

    def create_shape_from_element(self, elem, file_type):
        if file_type == 'xml':
            return self.create_shape_from_xml_elem(elem)
        elif file_type == 'json':
            return self.create_shape_from_json_elem(elem)

    def create_shape_from_xml_elem(self, elem):
        shape = self.xml_parser.parse(elem)
        if shape is not None:
            transforms = TransformFactory.create_transforms_from_xml_elem(elem)
            for transform in transforms:
                shape.apply_transform(transform)
        return shape

    def create_shape_from_json_elem(self, elem):
        shape = self.json_parser.parse(elem)
        if shape is not None:
            transforms = TransformFactory.create_transforms_from_json_elem(elem)
            for transform in transforms:
                shape.apply_transform(transform)
        return shape
