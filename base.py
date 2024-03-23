import base64
import os

import requests
from dotenv import load_dotenv

# Load environment variables from .env file.
# This is how we get the "username", "token", and "repo" values.
load_dotenv()


def create_auth_headers(token):
    """
    Factory to create authentication headers for GitHub API requests.

    :param token: GitHub personal access token for authentication
    :return: Dictionary with authorization and accept headers.
    """
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }


def create_base_url(username, repo):
    """
    Factory to create base URL for a GitHub API request.

    :param username: GitHub username
    :param repo: Repository name

    :return: Base URL for the GitHub API request.
    """
    return f"https://api.github.com/repos/{username}/{repo}/contents/"


def get_github_file_content(username, token, repo, path):
    """
    Fetch the content of a file from a GitHub repository.

    :param username: GitHub username
    :param token: GitHub personal access token for authentication
    :param repo: Repository name
    :param path: Path to the file within the repository
    :return: The content of the file as a string, or None if the request fails.
    """
    base_url = create_base_url(username, repo)
    url = base_url + path
    headers = create_auth_headers(token)
    print(f"Sending request to: {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        content = base64.b64decode(response.json()["content"]).decode("utf-8")
        return content
    else:
        return None


def list_github_files_in_path(username, token, repo, path):
    """
    List the files in a directory within a GitHub repository.

    Args:
        username (str): GitHub username
        token (str): GitHub personal access token for authentication
        repo (str): Repository name
        path (str): Path to the directory within the repository

    Returns:
        list: A list of file names in the directory, or None if the request fails.
    """
    base_url = create_base_url(username, repo)
    url = base_url + path
    headers = create_auth_headers(token)
    print(f"Sending request to: {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        items = response.json()
        file_names = [item["name"] for item in items if item["type"] == "file"]
        return file_names
    else:
        return None


def list_github_directories_in_path(username, token, repo, path):
    """
    List the directories in a path within a GitHub repository.

    Args:
        username (str): GitHub username
        token (str): GitHub personal access token for authentication
        repo (str): Repository name
        path (str): Path to the directory within the repository

    Returns:
        list: A list of directory names in the directory, or None if the request fails.
    """
    base_url = create_base_url(username, repo)
    url = base_url + path
    headers = create_auth_headers(token)
    print(f"Sending request to: {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        items = response.json()
        directory_names = [item["name"] for item in items if item["type"] == "dir"]
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
    file_content = get_github_file_content(file_to_get)

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
