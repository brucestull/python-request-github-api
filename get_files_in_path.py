# get_files_in_path.py

from base import list_files_in_path
import pprint

directory_path = "unimportant_notes"

files = list_files_in_path(directory_path)

if files:
    print(f"\nFiles in '{directory_path}':\n")
    pprint.pprint(files)
else:
    print(f"Files in '{directory_path}' not found or unable to fetch.")
