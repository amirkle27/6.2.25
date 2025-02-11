from abc import ABC,abstractmethod
from importlib.metadata import files


class ComponentRecursive(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def draw(self, indent=0):
        pass





