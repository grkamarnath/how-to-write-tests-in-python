from unittest.mock import Mock
from requests.exceptions import HTTPError
import pytest

from gateway import GithubAPI
from main import get_response, is_even_number



def test_get_response():
    mock_client = Mock(spec=GithubAPI)
    get_response(mock_client)
    mock_client.get_github_response.assert_called_once()


def test_get_response_raises_http_error():
    mock_client = Mock(spec=GithubAPI)
    mock_client.get_github_response.side_effect = HTTPError
    with pytest.raises(HTTPError):
        get_response(mock_client)

def test_is_even_number_method_by_passing_four_and_expecting_true():
    expected_data = True
    actual_data = is_even_number(4)
    assert expected_data == actual_data

def test_is_even_number_method_by_passing_five_and_expecting_false():
    expected_data = False
    actual_data = is_even_number(5)
    assert expected_data == actual_data
