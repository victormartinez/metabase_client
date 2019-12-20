from metabase_client.http import HttpClient
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
        self.session_resource = SessionResource(HttpClient(endpoint))
        self.card_resource = CardResource(HttpClient(endpoint))

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
        if not all([self.username, self.password]):
            raise MetabaseConfigError("You must provide username and password.")

        try:
            idx = self.session_resource.get_token(self.username, self.password)
            if not idx:
                raise MetabaseAuthError(
                    "The endpoint did not return a valid credential."
                )
            self.token = idx
        except Exception as exc:
            raise MetabaseAuthError(repr(exc))

    def get_cards(self):
        try:
            return self.card_resource.list(self.token)
        except Exception as exc:
            raise MetabaseRequestError(repr(exc))
