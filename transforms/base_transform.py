from abc import ABC, abstractmethod


class ITransform(ABC):
    @abstractmethod
    def apply(self, *args, **kwargs):
        pass
