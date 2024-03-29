# get_directories_in_path.py

import os
import pprint

from dotenv import load_dotenv

from base import GitHubAPI

load_dotenv()

username = os.getenv("USERNAME")
token = os.getenv("TOKEN")
repo = os.getenv("REPO")

directory_path = "unimportant_notes"
directory_path = ""

api = GitHubAPI(username, token, repo)

directories = api.list_directories_in_path(directory_path)

if directories:
    print(f"\nDirectories in '{directory_path}':\n")
    pprint.pprint(directories)
else:
    print(f"Directories in '{directory_path}' not found or unable to fetch.")
