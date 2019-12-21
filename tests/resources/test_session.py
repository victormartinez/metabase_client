import mock

from metabasepy.resources import SessionResource


def test_get_token():
    mock_client = mock.Mock()
    mock_client.request.return_value = mock.Mock(json=lambda: {"id": "1q2w3e4r"})

    resource = SessionResource(mock_client)
    assert resource.get_token("user", "pass") == "1q2w3e4r"
    mock_client.request.assert_called_once_with(
        "post",
        "/api/session",
        headers={"Content-Type": "application/json"},
        json={"username": "user", "password": "pass"},
    )
