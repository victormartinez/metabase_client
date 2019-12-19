import pytest
import mock
from requests.exceptions import RequestException

from metabase_client.client import MetabaseClient
from metabase_client.exceptions import MetabaseAuthError, MetabaseConfigError


@mock.patch("requests.request")
def test_success(mock_request):
    mock_request.return_value = mock.Mock(json=lambda: {"id": "1q2w3e4r5t"})
    client = MetabaseClient("https://endpoint", username="user", password="pass")
    client.auth()

    assert client.token == "1q2w3e4r5t"


def test_no_credentials_provided():
    client = MetabaseClient("https://endpoint", token="token")
    with pytest.raises(MetabaseConfigError):
        client.auth()


@mock.patch("requests.request")
def test_no_token_returned(mock_request):
    mock_request.return_value = mock.Mock(json=lambda: {"data": "teste"})
    client = MetabaseClient("https://endpoint", username="user", password="pass")

    with pytest.raises(MetabaseAuthError) as exc:
        client.auth()

    assert str(exc.value) == "MetabaseAuthError('The endpoint did not return a valid credential.')"


@mock.patch("requests.request")
def test_request_exception(mock_request):
    mock_request.side_effect = RequestException("Request error")

    client = MetabaseClient("https://endpoint", username="user", password="pass")
    with pytest.raises(MetabaseAuthError) as exc:
        client.auth()

    assert str(exc.value) == "RequestException('Request error')"
