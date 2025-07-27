import xml.etree.ElementTree as ET
from shape_factory import ShapeFactory


class Scene:
    def __init__(self):
        self.shapes = []

    def load_from_file(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()

        for elem in root:
            shape = ShapeFactory.create_shape(elem)
            self.shapes.append(shape)

    def render(self):
        for shape in self.shapes:
            shape.draw()
