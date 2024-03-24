# get_files_in_path.py

import os
import pprint

from dotenv import load_dotenv

from base import GitHubAPI

load_dotenv()

username = os.getenv("USERNAME")
token = os.getenv("TOKEN")
repo = os.getenv("REPO")

directory_path = "unimportant_notes"

api = GitHubAPI(username, token, repo)

files = api.list_files_in_path(directory_path)

if files:
    print(f"\nFiles in '{directory_path}':\n")
    pprint.pprint(files)
else:
    print(f"Files in '{directory_path}' not found or unable to fetch.")
