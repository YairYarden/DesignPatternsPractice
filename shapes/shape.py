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

    @abstractmethod
    def draw(self):
        pass

    def transform(self, transformation: ITransform):
        transformed_points = transformation.apply(self.get_points())
        self.set_points(transformed_points)
