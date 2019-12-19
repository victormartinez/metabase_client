from json.decoder import JSONDecodeError
from urllib.parse import urljoin

from metabase_client.resources import CardResource, SessionResource

from metabase_client.exceptions import (
    MetabaseAuthError,
    MetabaseConfigError,
    MetabaseRequestError,
)


class MetabaseClient:
    def __init__(self, endpoint, **kwargs):
        self.token = None
        self.username = None
        self.password = None
        self.session_resource = SessionResource(endpoint)
        self.card_resource = CardResource(endpoint)

        for key, value in kwargs.items():
            if not hasattr(self, key):
                raise MetabaseConfigError(f"The argument {key} is not valid.")
            setattr(self, key, value)

        if (
            not self.token
            and not all([self.username, self.password])
            or not endpoint
            or not kwargs.items()
        ):
            raise MetabaseConfigError("Invalid arguments provided.")

    def auth(self):
        try:
            self.token = self.session_resource.get_token(self.username, self.password)
        except Exception as exc:
            raise MetabaseAuthError(repr(msg))

    def get_cards(self):
        try:
            return self.card_resource.list(self.token)
        except Exception as exc:
            raise MetabaseRequestError(repr(msg))
