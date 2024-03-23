# GitHub API File List

[GitHub API File List - ChatGPT](https://chat.openai.com/share/845d1b9f-95c7-458e-a16c-d8b2ee145780)

## Request

I have a python script which used GitHub API:

```python
import base64
import os

import requests
from dotenv import load_dotenv

# Load environment variables from .env file.
# This is how we get the "USERNAME", "TOKEN", and "REPO" values.
load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
REPO = os.getenv("REPO")
BASE_URL = f"https://api.github.com/repos/{USERNAME}/{REPO}/contents/"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}


def get_file_content(path):
    url = BASE_URL + path
    print(f"Sending request to: {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        content = base64.b64decode(response.json()["content"]).decode("utf-8")
        return content
    else:
        return None


# file_to_get = "Pipfile"
# file_to_get = "notes/debug_works_but_cli_doesnt.md"
file_to_get = "unimportant_notes/models.py"
# file_to_get = "models.py"


# gitignore_content = get_file_content('.gitignore')
# urls_content = get_file_content('config/urls.py')
file_content = get_file_content(file_to_get)

# if gitignore_content:
#     print("Contents of .gitignore:\n", gitignore_content)
# else:
#     print(".gitignore not found or unable to fetch.")

# if urls_content:
#     print("\nContents of 'config/urls.py':\n", urls_content)
# else:
#     print("'config/urls.py' not found or unable to fetch.")

if file_content:
    print(f"\nContents of '{file_to_get}':\n\n", file_content)
else:
    print(f"'{file_to_get}' not found or unable to fetch.")
```

Help me add a method to get a list of the files in a specific directory in a repository?

## Response

To extend your script to include a method for listing the files in a specific directory of a repository, you can utilize the GitHub API's functionality for accessing repository contents. This method will make a GET request to the repository's contents endpoint, specifying a path to the directory of interest. If the path corresponds to a directory, the GitHub API returns a JSON array containing objects for each item in the directory.

Here's how you can add a method named `list_files_in_directory` to your existing script:

```python
def list_files_in_directory(path):
    url = BASE_URL + path
    print(f"Sending request to: {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        files = response.json()
        file_names = [file["name"] for file in files if file["type"] == "file"]
        return file_names
    else:
        return None

# Example usage:
directory_path = "path/to/directory"  # Replace with your target directory path
files = list_files_in_directory(directory_path)
if files:
    print(f"Files in '{directory_path}':\n", "\n".join(files))
else:
    print(f"No files found in '{directory_path}' or unable to fetch.")
```

This method constructs a URL using the base URL, the username, the repository name, and the path to the directory you're interested in. It sends a GET request to this URL and checks the response status code. If the response code is 200 (OK), it processes the JSON response to extract the names of the files in the specified directory. Note that this method filters the results to include only items of type `"file"`, ignoring directories and subdirectories.

Remember to replace `"path/to/directory"` with the actual path of the directory you want to list the files from. The GitHub API is quite powerful, and this is just one of the many things you can do with it to interact with repositories programmatically.
