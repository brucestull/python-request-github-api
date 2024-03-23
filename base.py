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


def list_files_in_path(path):
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


def list_directories_in_path(path):
    url = BASE_URL + path
    print(f"Sending request to: {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        files = response.json()
        directory_names = [file["name"] for file in files if file["type"] == "dir"]
        return directory_names
    else:
        return None


def main():

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


if __name__ == "__main__":
    main()
