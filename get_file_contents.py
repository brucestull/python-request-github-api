# get_file_contents.py

import os

from dotenv import load_dotenv

from base import get_github_file_content

load_dotenv()

username = os.getenv("USERNAME")
token = os.getenv("TOKEN")
repo = os.getenv("REPO")

file_to_get = "unimportant_notes/models.py"

file_content = get_github_file_content(username, token, repo, file_to_get)

if file_content:
    print(f"\nContents of '{file_to_get}':\n", file_content)
else:
    print(f"'{file_to_get}' not found or unable to fetch.")
