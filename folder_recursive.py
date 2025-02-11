import os

from bonus_component import ComponentRecursive
from typing import override

class FolderRecursive(ComponentRecursive):

    def __init__(self, folder_name):
        super().__init__(folder_name)
        self.children = []


    def add_folder(self, folder):
        self.children.append(folder)

    def add_file(self, file):
        self.children.append(file)

    @override
    def draw(self, indent = 0):
        print(f"{' ' * indent}[{self.name}]")
        for child in self.children:
            child.draw(indent+4)
