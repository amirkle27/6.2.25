import os

from bonus_component import ComponentRecursive
from typing import override


class FileRecursive(ComponentRecursive):

    def __init__(self, file_name, file_size):
        super().__init__(file_name)
        self.size = file_size

    @override
    def draw(self, indent=0):
        print(f"{' ' * indent}- {self.name} ({self.size})")






