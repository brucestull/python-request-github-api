# get_files_in_directory.py

import os

from dotenv import load_dotenv

from base import GitHubAPI

from pprint import pprint

load_dotenv()

username = os.getenv("USERNAME")
token = os.getenv("TOKEN")
repo = os.getenv("REPO")

# Start in the root directory of the project:
initial_directory = ""

# Instantiate the GitHubAPI class:
api = GitHubAPI(username, token, repo)

# Get the directories in the initial directory:
directories = api.list_directories_in_path(initial_directory)

# Print the directories:
if directories:
    print(f"\nDirectories in '{initial_directory}':\n")
    pprint(directories)
else:
    print(f"Directories in '{initial_directory}' not found or unable to fetch.")

# Iterate over the directories:
for directory in directories:
    # Check if the directory contains an `apps.py` file:
    contains_apps_dot_py = api.check_directory_contains_apps_dot_py(directory)
    if contains_apps_dot_py:
        print(f"\n'{directory}' is a Django application.")
        # Get contents of the `apps.py` file:
        apps_py_file = f"{directory}/apps.py"
        apps_py_content = api.get_file_content(apps_py_file)
        if apps_py_content:
            print(f"\nContents of '{apps_py_file}':\n", apps_py_content)
        else:
            print(f"'{apps_py_file}' not found or unable to fetch.")
    else:
        print(f"\n'{directory}' is NOT a Django application.")


# # Get the files in the initial directory:
# files = api.list_files_in_path(initial_directory)

# # Print the files:
# if files:
#     print(f"\nFiles in '{initial_directory}':\n")
#     pprint(files)
# else:
#     print(f"Files in '{initial_directory}' not found or unable to fetch.")
