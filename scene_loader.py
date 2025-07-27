import xml.etree.ElementTree as ET
from shape_factory import ShapeFactory
import cv2

class Scene:
    def __init__(self):
        self.shapes = []

    def load_from_file(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()

        for elem in root:
            shape = ShapeFactory.create_shape(elem)
            self.shapes.append(shape)

    def render(self, canvas):
        for shape in self.shapes:
            shape.draw(canvas)

    @staticmethod
    def show_scene(canvas):
        cv2.imshow("Scene", canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()