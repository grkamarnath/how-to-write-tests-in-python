from requests.exceptions import HTTPError
import requests


class GithubAPI:
    def get_github_response(self):
        response = requests.get("https://api.github.com")
        try:
            response.raise_for_status()
            return response
        except HTTPError as error:
            raise error
