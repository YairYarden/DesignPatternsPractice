from parsers.xml_shape_parser import XmlShapeParser
from parsers.json_shape_parser import JsonShapeParser


class ShapeFactory:

    def __init__(self):
        self.composites = {}
        self.xml_parser = XmlShapeParser(self)
        self.json_parser = JsonShapeParser(self)

    def create_shape_from_xml_elem(self, elem):
        return self.xml_parser.parse(elem)

    def create_shape_from_json_elem(self, elem):
        return self.json_parser.parse(elem)
