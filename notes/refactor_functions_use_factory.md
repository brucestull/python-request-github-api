# Refactor Functions, Use Factory

[Refactor Functions, Use Factory - ChatGPT](https://chat.openai.com/share/ea1cb9d0-f6bd-4e1d-8e96-d5d0676c6660)

## Request

I have a couple python functions:

```python
def get_github_file_content(username, token, repo, path):
    """
    Fetch the content of a file from a GitHub repository.

    :param username: GitHub username
    :param token: GitHub personal access token for authentication
    :param repo: Repository name
    :param path: Path to the file within the repository
    :return: The content of the file as a string, or None if the request fails.
    """
    base_url = f"https://api.github.com/repos/{username}/{repo}/contents/"
    url = base_url + path
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
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
    base_url = f"https://api.github.com/repos/{username}/{repo}/contents/"
    url = base_url + path
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    print(f"Sending request to: {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        items = response.json()
        file_names = [item["name"] for item in items if item["type"] == "file"]
        return file_names
    else:
        return None
```

Is there a way i can take the `headers` in each of those functions and extract them into some form of callback or some other way to pass them as an argument?

## Response

Yes, you can refactor your code to use a higher-order function or a callback mechanism to handle the creation and passing of the headers. This approach allows you to define the headers in one place and reuse them across different functions, thus making your code more DRY (Don't Repeat Yourself). Here's an example of how you can do this:

### Step 1: Define a Higher-Order Function for Headers
Create a function that takes in the authentication details (username and token) and returns a dictionary with the headers. This function serves as a factory for creating headers.

```python
def create_auth_headers(username, token):
    """
    Create authentication headers for GitHub API requests.

    :param username: GitHub username
    :param token: GitHub personal access token for authentication
    :return: Dictionary with authorization and accept headers.
    """
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
```

### Step 2: Refactor Existing Functions to Use the Headers Factory
Adjust your existing functions to use the `create_auth_headers` function to get their headers. This means you'll pass the `username` and `token` to `create_auth_headers` inside each function and use its return value as the headers for the requests.

```python
import requests
import base64

def get_github_file_content(username, token, repo, path):
    """
    Fetch the content of a file from a GitHub repository.
    """
    base_url = f"https://api.github.com/repos/{username}/{repo}/contents/"
    url = base_url + path
    headers = create_auth_headers(username, token)
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
    """
    base_url = f"https://api.github.com/repos/{username}/{repo}/contents/"
    url = base_url + path
    headers = create_auth_headers(username, token)
    print(f"Sending request to: {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        items = response.json()
        file_names = [item["name"] for item in items if item["type"] == "file"]
        return file_names
    else:
        return None
```

This refactoring allows you to maintain the headers creation logic in one place, making your code cleaner and easier to maintain. If you need to update the headers in the future (for example, to use a new version of the GitHub API), you'll only need to make changes in one place.
