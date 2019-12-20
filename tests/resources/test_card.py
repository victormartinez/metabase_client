import mock

from metabase_client.resources import CardResource


def test_get_cards():
    mock_client = mock.Mock()
    mock_client.authenticated.return_value = (
        mock.Mock(json=lambda: [{"id": 1, "rows": []}])
    )

    resource = CardResource(mock_client)
    assert resource.list("1q2w3e4r") == [{"id": 1, "rows": []}]
    mock_client.authenticated.assert_called_once_with(
        "get", "/api/card", "1q2w3e4r"
    )

