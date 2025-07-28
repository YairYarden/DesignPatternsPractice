from transforms.translation import TranslationX, TranslationY
from transforms.scaling import Scaling
from transforms.rotation import Rotation


class TransformFactory:

    @staticmethod
    def create_transforms(elem):
        scale_factor = float(elem.attrib.get("Scale", 1.0))
        dx = float(elem.attrib.get("TranslateX", 0))
        dy = float(elem.attrib.get("TranslateY", 0))
        angle = float(elem.attrib.get("Rotate", 0))
        transforms = [Scaling(scale_factor), TranslationX(dx), TranslationY(dy), Rotation(angle)]
        return transforms
