import pytest

from metabase_client.client import MetabaseClient
from metabase_client.exceptions import MetabaseConfigError


@pytest.mark.parametrize("endpoint,username,password,token", [
    (None, None, None, None),
    ("", "", "", ""),
    ("http://metabase.com", "", "", ""),
    ("http://metabase.com", "username", "", ""),
    ("http://metabase.com", "", "password", ""),
    ("", "username", "", ""),
    ("", "", "password", ""),
    ("", "", "", "token"),
    ("", "username", "password", ""),
    ("", "", "password", "token"),
    ("http://metabase.com", "username", "", ""),
    ("http://metabase.com", "username", "", ""),
    ("http://metabase.com", "", "password", ""),
])
def test_config_error(endpoint, username, password, token):
    with pytest.raises(MetabaseConfigError):
        MetabaseClient(endpoint, username=username, password=password, token=token)


@pytest.mark.parametrize("endpoint,username,password,token", [
    ("http://metabase.com", "username", "password", ""),
    ("http://metabase.com", "username", "password", "token"),
    ("http://metabase.com", "", "", "token"),
    ("http://metabase.com", "", "password", "token"),
    ("http://metabase.com", "username", "", "token"),
])
def test_config_success(endpoint, username, password, token):
    client = MetabaseClient(
        endpoint, username=username, password=password, token=token
    )
    assert client is not None
