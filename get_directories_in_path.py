# get_directories_in_path.py

from base import list_directories_in_path
import pprint

directory_path = "unimportant_notes"

directories = list_directories_in_path(directory_path)

if directories:
    print(f"\nDirectories in '{directory_path}':\n")
    pprint.pprint(directories)
else:
    print(f"Directories in '{directory_path}' not found or unable to fetch.")
