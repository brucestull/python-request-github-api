# get_files_in_path.py

import os
import pprint

from dotenv import load_dotenv

from base import list_github_files_in_path

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
REPO = os.getenv("REPO")

directory_path = "unimportant_notes"

files = list_github_files_in_path(USERNAME, TOKEN, REPO, directory_path)

if files:
    print(f"\nFiles in '{directory_path}':\n")
    pprint.pprint(files)
else:
    print(f"Files in '{directory_path}' not found or unable to fetch.")
