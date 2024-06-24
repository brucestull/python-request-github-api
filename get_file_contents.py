# get_file_contents.py

import os

from dotenv import load_dotenv

from base import GitHubAPI

# Load environment variables:
load_dotenv()  # This line isn't needed when running with VS Code Debug Configuration
username = os.getenv("USERNAME")
token = os.getenv("TOKEN")
repo = os.getenv("REPO")

# Relative path to the file within the repository:
file_to_get = "runner.py"
# file_to_get = "manage.py"

api = GitHubAPI(username, token, repo)

file_content = api.get_file_content(file_to_get)

if file_content:
    print(f"\nContents of '{file_to_get}':\n", file_content)
else:
    print(f"'{file_to_get}' not found or unable to fetch.")
