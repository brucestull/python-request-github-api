# get_directories_containing_apps_dot_py.py

import os
import pprint

from dotenv import load_dotenv

from base import GitHubAPI

# Load environment variables:
load_dotenv()  # This line isn't needed when running with VS Code Debug Configuration
username = os.getenv("USERNAME")
token = os.getenv("TOKEN")
repo = os.getenv("REPO")

# Specify the directory path:
directory_path = ""

# Specify the file to check for:
check_file = "apps.py"
# check_file = "models.py"

# Instantiate the GitHubAPI class:
api = GitHubAPI(username, token, repo)

directories = api.list_directories_containing_file(directory_path, check_file)

if directories:
    print(f"\nDirectories containing '{check_file}' in '{directory_path}':\n")
    pprint.pprint(directories)
else:
    print(
        f"Directories containing '{check_file}' in '{directory_path}' not found or "
        f"unable to fetch."
    )
