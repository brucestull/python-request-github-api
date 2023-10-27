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


file_to_get = "Pipfile"


# gitignore_content = get_file_content('.gitignore')
# urls_content = get_file_content('config/urls.py')
boops_models_content = get_file_content(file_to_get)

# if gitignore_content:
#     print("Contents of .gitignore:\n", gitignore_content)
# else:
#     print(".gitignore not found or unable to fetch.")

# if urls_content:
#     print("\nContents of 'config/urls.py':\n", urls_content)
# else:
#     print("'config/urls.py' not found or unable to fetch.")

if boops_models_content:
    print(f"\nContents of '{file_to_get}':\n\n", boops_models_content)
else:
    print(f"'{file_to_get}' not found or unable to fetch.")
