from bonus_component import ComponentRecursive
from folder_recursive import FolderRecursive
from file_recursive import FileRecursive
import os
from pip._internal.utils.misc import format_size


def list_files_recc(folder_path):
    root_folder_name = os.path.basename(folder_path)
    root_folder = FolderRecursive(root_folder_name)

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        if os.path.isdir(full_path):
            if not item.startswith('.') and not item.startswith('__'):
                sub_folder = list_files_recc(full_path)  # Recursively build the subfolder
                root_folder.add_folder(sub_folder)  # Add subfolder to current folder
        else:
            size = format_size(os.path.getsize(full_path))
            file = FileRecursive(item, size)
            root_folder.add_file(file)  # Add file to current folder

    return root_folder  # Return the folder composite



if __name__ == "__main__":
    root = list_files_recc(r"C:\Users\123\Downloads")
    root.draw()