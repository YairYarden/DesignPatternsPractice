from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def from_xml(cls, element):
        pass

    @abstractmethod
    def draw(self):
        pass
