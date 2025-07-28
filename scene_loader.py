import xml.etree.ElementTree as ET
import json
from shapes.shape_factory import ShapeFactory
from transforms.transform_factory import TransformFactory
import cv2


class Scene:
    def __init__(self):
        self.shapes = []
        self.shape_factory = ShapeFactory()

    def load_from_file(self, filename):
        extension = filename.rsplit('.', 1)[-1] if '.' in filename else ''
        if extension == "xml":
            self.load_from_xml(filename)
        elif extension == "json":
            self.load_from_json(filename)
        else:
            raise ValueError(f"No support in file type : {extension}")

    def load_from_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        for elem in root:
            shape = self.shape_factory.create_shape_from_xml_elem(elem)
            if shape is not None:
                transforms = TransformFactory.create_transforms_from_xml_elem(elem)
                for transform in transforms:
                    shape.apply_transform(transform)
                self.shapes.append(shape)

    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            json_data = json.load(file)

        for entry in json_data:
            shape = self.shape_factory.create_shape_from_json_elem(entry)
            if shape is not None:
                transforms = TransformFactory.create_transforms_from_json_elem(entry)
                for transform in transforms:
                    shape.apply_transform(transform)
                self.shapes.append(shape)

    def render(self, canvas):
        for shape in self.shapes:
            shape.draw(canvas)

    @staticmethod
    def show_scene(canvas):
        cv2.imshow("Scene", canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
