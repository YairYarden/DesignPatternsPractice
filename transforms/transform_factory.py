from transforms.translation import TranslationX, TranslationY
from transforms.scaling import Scaling
from transforms.rotation import Rotation


class TransformFactory:
    @staticmethod
    def create_transforms(elem, file_type):
        if file_type == 'xml':
            return TransformFactory.create_transforms_from_xml_elem(elem)
        elif file_type == 'json':
            return TransformFactory.create_transforms_from_json_elem(elem)
        else:
            raise ValueError(f"No support in File type : {file_type}")

    @staticmethod
    def create_transforms_from_xml_elem(elem):
        scale_factor = float(elem.attrib.get("Scale", 1.0))
        dx = float(elem.attrib.get("TranslateX", 0))
        dy = float(elem.attrib.get("TranslateY", 0))
        angle = float(elem.attrib.get("Rotate", 0))
        transforms = [Scaling(scale_factor), TranslationX(dx), TranslationY(dy), Rotation(angle)]
        return transforms

    @staticmethod
    def create_transforms_from_json_elem(elem):
        scale_factor = float(elem.get("scale", 1.0))
        dx = int(elem.get("translate_x", 0))
        dy = int(elem.get("translate_y", 0))
        angle = float(elem.get("rotate", 0))
        transforms = [Scaling(scale_factor), TranslationX(dx), TranslationY(dy), Rotation(angle)]
        return transforms
