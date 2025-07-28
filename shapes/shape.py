from abc import ABC, abstractmethod
from transforms.base_transform import ITransform


class Shape(ABC):
    @abstractmethod
    def get_points(self) -> list[tuple[int, int]]:
        pass

    @abstractmethod
    def set_points(self, new_points: list[tuple[int, int]]):
        pass

    @abstractmethod
    def apply_transform(self, transform: ITransform):
        pass

    def compute_center_mass(self):
        points = self.get_points()
        x_all = [p[0] for p in points]
        y_all = [p[1] for p in points]
        return int(sum(x_all) / len(points)), int(sum(y_all) / len(points))

    @abstractmethod
    def draw(self):
        pass

    def transform(self, transformation: ITransform):
        transformed_points = transformation.apply(self.get_points())
        self.set_points(transformed_points)
