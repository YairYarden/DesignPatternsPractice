import xml.etree.ElementTree as ET
import json
from shapes.shape_factory import ShapeFactory
from transforms.transform_factory import TransformFactory
import cv2


class Scene:
    def __init__(self, filename):
        self.shapes = []
        self.shape_factory = ShapeFactory()
        self.filename = filename
        self.extension = filename.rsplit('.', 1)[-1] if '.' in filename else ''

    def load_from_file(self):
        if self.extension == "xml":
            self.load_from_xml(self.filename)
        elif self.extension == "json":
            self.load_from_json(self.filename)
        else:
            raise ValueError(f"No support in file type : {self.extension}")

    def load_from_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        self.load_from_file_obj(root)

    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            json_data = json.load(file)
        self.load_from_file_obj(json_data)

    def load_from_file_obj(self, file_obj):
        for elem in file_obj:
            shape = self.shape_factory.create_shape_from_element(elem, self.extension)
            if shape is not None:
                self.shapes.append(shape)

    def render(self, canvas):
        for shape in self.shapes:
            shape.draw(canvas)

    @staticmethod
    def show_scene(canvas):
        cv2.imshow("Scene", canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
