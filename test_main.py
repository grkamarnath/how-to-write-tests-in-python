from unittest.mock import Mock
from requests.exceptions import HTTPError
import pytest

from gateway import GithubAPI
from main import get_response



def test_get_response():
    mock_client = Mock(spec=GithubAPI)
    get_response(mock_client)
    mock_client.get_github_response.assert_called_once()


def test_get_response_raises_http_error():
    mock_client = Mock(spec=GithubAPI)
    mock_client.get_github_response.side_effect = HTTPError
    with pytest.raises(HTTPError):
        get_response(mock_client)
