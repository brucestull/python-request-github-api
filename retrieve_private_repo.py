import requests
import base64
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

USERNAME = os.getenv('USERNAME')
TOKEN = os.getenv('TOKEN')
REPO = os.getenv('REPO')
BASE_URL = f'https://api.github.com/repos/{USERNAME}/{REPO}/contents/'

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}


def get_file_content(path):
    response = requests.get(BASE_URL + path, headers=headers)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        content = base64.b64decode(response.json()['content']).decode('utf-8')
        return content
    else:
        return None


gitignore_content = get_file_content('.gitignore')
urls_content = get_file_content('config/urls.py')

if gitignore_content:
    print("Contents of .gitignore:\n", gitignore_content)
else:
    print(".gitignore not found or unable to fetch.")

if urls_content:
    print("\nContents of config/urls.py:\n", urls_content)
else:
    print("config/urls.py not found or unable to fetch.")
