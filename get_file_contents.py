# get_file_contents.py

import os

from dotenv import load_dotenv

from base import GitHubAPI

load_dotenv()

username = os.getenv("USERNAME")
token = os.getenv("TOKEN")
repo = os.getenv("REPO")

file_to_get = "unimportant_notes/models.py"

api = GitHubAPI(username, token, repo)

file_content = api.get_file_content(file_to_get)

if file_content:
    print(f"\nContents of '{file_to_get}':\n", file_content)
else:
    print(f"'{file_to_get}' not found or unable to fetch.")
