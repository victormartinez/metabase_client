import pytest
import mock
from requests.exceptions import RequestException

from metabasepy.client import MetabaseClient
from metabasepy.exceptions import MetabaseRequestError


@mock.patch("requests.request")
def test_success(mock_request):
    mock_request.return_value = mock.Mock(json=lambda: [{"id": 1, "rows": []}])
    client = MetabaseClient("https://endpoint", token="1q2w3e4r5t")
    cards = client.get_cards()

    assert cards == [{"id": 1, "rows": []}]


@mock.patch("requests.request")
def test_request_exception(mock_request):
    mock_request.side_effect = RequestException("Request error")
    client = MetabaseClient("https://endpoint", token="1q2w3e4r5t")
    with pytest.raises(MetabaseRequestError) as exc:
        client.get_cards()

    assert str(exc.value) == "RequestException('Request error')"
