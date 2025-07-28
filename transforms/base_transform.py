from abc import ABC, abstractmethod


class ITransform(ABC):
    @abstractmethod
    def apply(self, points: list[tuple[int, int]]) -> list[tuple[int, int]]:
        pass
