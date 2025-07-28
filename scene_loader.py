import xml.etree.ElementTree as ET
import json
from shapes.shape_factory import ShapeFactory
import cv2


class Scene:
    def __init__(self, filename):
        self.shapes = []
        self.filename = filename
        self.extension = filename.rsplit('.', 1)[-1] if '.' in filename else ''
        self.shape_factory = ShapeFactory(self.extension)

    def load_from_file(self):
        if self.extension == "xml":
            self.load_from_xml()
        elif self.extension == "json":
            self.load_from_json()
        else:
            raise ValueError(f"No support in file type : {self.extension}")

    def load_from_xml(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        self.load_from_file_obj(root)

    def load_from_json(self):
        with open(self.filename, 'r') as file:
            json_data = json.load(file)
        self.load_from_file_obj(json_data)

    def load_from_file_obj(self, file_obj):
        for elem in file_obj:
            shape = self.shape_factory.create_shape_from_element(elem)
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
