import xml.etree.ElementTree as ET
from shape_factory import ShapeFactory
from transforms.transform_factory import TransformFactory
import cv2


class Scene:
    def __init__(self):
        self.shapes = []

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
            shape = ShapeFactory.create_shape(elem)
            transforms = TransformFactory.create_transforms(elem)
            for transform in transforms:
                shape.set_points(transform.apply(shape.get_points()))
            self.shapes.append(shape)

    def load_from_json(self, filename):
        pass

    def render(self, canvas):
        for shape in self.shapes:
            shape.draw(canvas)

    @staticmethod
    def show_scene(canvas):
        cv2.imshow("Scene", canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
