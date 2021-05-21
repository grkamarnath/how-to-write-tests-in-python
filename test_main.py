from unittest.mock import Mock
from requests.exceptions import HTTPError
import pytest

from gateway import GithubAPI
from main import get_response



def test_get_response():
    mock_clinet = Mock(spec=GithubAPI)
    get_response(mock_clinet)
    mock_clinet.get_github_response.assert_called_once()


def test_get_response_raises_http_error():
    mock_clinet = Mock(spec=GithubAPI)
    mock_clinet.get_github_response.side_effect = HTTPError
    with pytest.raises(HTTPError):
        get_response(mock_clinet)
