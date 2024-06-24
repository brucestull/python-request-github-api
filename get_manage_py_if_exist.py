# get_manage_py_if_exist.py

import os

from dotenv import load_dotenv

from base import GitHubAPI

from pprint import pprint

# Load environment variables:
load_dotenv()  # This line isn't needed when running with VS Code Debug Configuration
username = os.getenv("USERNAME")
token = os.getenv("TOKEN")
repo = os.getenv("REPO")

# Start in the root directory of the project:
initial_path = ""

# Specify the file to check for:
check_file = "manage.py"

# Instantiate the GitHubAPI class:
api = GitHubAPI(username, token, repo)

# Use `check_directory_contains_file` to get the directories containing `manage.py`:
manage_py_directories = api.list_directories_containing_file(initial_path, check_file)

# Print the directories containing `manage.py`:
if manage_py_directories:
    print(f"\nDirectories containing '{check_file}' in '{initial_path}':\n")
    pprint(manage_py_directories)
