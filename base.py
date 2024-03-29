import base64
import os
import requests
from dotenv import load_dotenv


class GitHubAPI:
    def __init__(self, username, token, repo):
        """
        Initializes the GitHubAPI class with user credentials and repository information.

        Args:
            username (str): GitHub username
            token (str): GitHub personal access token for authentication
            repo (str): Repository name
        """
        self.username = username
        self.token = token
        self.repo = repo
        self.base_url = (
            f"https://api.github.com/repos/{self.username}/{self.repo}/contents/"
        )
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
        }

    def _request(self, path, method="GET"):
        """
        Internal method to make a GitHub API request.

        Args:
            path (str): Relative path to the file or directory within the repository
            method (str): HTTP method (e.g., "GET")

        Returns:
            The JSON response as a dictionary, or None if the request fails.
        """
        url = self.base_url + path
        print(f"Sending request to: {url}")
        response = requests.request(method, url, headers=self.headers)
        print(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_file_content(self, path):
        """
        Sends API request to fetch the content of a file from the GitHub repository.

        Args:
            path (str): Path to the file within the repository

        Returns:
            The content of the file as a string, or None if the request fails.
        """
        response = self._request(path)
        if response:
            content = base64.b64decode(response["content"]).decode("utf-8")
            return content
        return None

    def list_directories_in_path(self, path):
        """
        Sends API request to list the directories in a path within the GitHub repository.

        Args:
            path (str): Path to the directory within the repository

        Returns:
            A list of directory names in the directory, or None if the request fails.
        """
        response = self._request(path)
        if response:
            directory_names = [
                item["name"] for item in response if item["type"] == "dir"
            ]
            return directory_names
        return None

    def list_files_in_path(self, path):
        """
        Sends an API request to list the files in a directory within the GitHub repository.

        Args:
            path (str): Path to the directory within the repository

        Returns:
            A list of file names in the directory, or None if the request fails.
        """
        response = self._request(path)
        if response:
            file_names = [item["name"] for item in response if item["type"] == "file"]
            return file_names
        return None

    def check_directory_contains_file(self, path, check_file):
        """
        Check if the directory contains check_file.

        Args:
            path (str): Path to the directory within the repository
            check_file (str): File to check for in the directory

        Returns:
            True if the directory contains check_file, False otherwise.
        """
        files = self.list_files_in_path(path)
        if files:
            return check_file in files
        return False

    def list_directories_containing_file(self, path, check_file):
        """
        Sends API request, via `list_directories_in_path`, and returns a list of the directories that contain check_file.

        Args:
            path (str): Path to the directory within the repository
            check_file (str): File to check for in the directory

        Returns:
            A list of directory names that contains check_file.
        """
        directories = self.list_directories_in_path(path)
        if directories:
            return [
                directory
                for directory in directories
                if self.check_directory_contains_file(directory, check_file)
            ]
        return []

    def __str__(self):
        return f"GitHubAPI for user {self.username} and repository {self.repo}"
