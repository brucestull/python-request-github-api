# get_files_in_path.py

import os
import pprint

from dotenv import load_dotenv

from base import GitHubAPI

# Load environment variables:
load_dotenv()  # This line isn't needed when running with VS Code Debug Configuration
username = os.getenv("USERNAME")
token = os.getenv("TOKEN")
repo = os.getenv("REPO")

# path = "unimportant_notes"
path = ""

api = GitHubAPI(username, token, repo)

files = api.list_files_in_path(path)

if files:
    print(f"\nFiles in '{path}':\n")
    pprint.pprint(files)
else:
    print(f"Files in '{path}' not found or unable to fetch.")
