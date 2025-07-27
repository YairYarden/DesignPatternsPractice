from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def read_from_xml(cls, element):
        pass

    @abstractmethod
    def draw(self):
        pass
