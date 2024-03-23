# get_file_contents.py

from base import get_file_content

file_to_get = "unimportant_notes/models.py"

file_content = get_file_content(file_to_get)

if file_content:
    print(f"\nContents of '{file_to_get}':\n", file_content)
else:
    print(f"'{file_to_get}' not found or unable to fetch.")
