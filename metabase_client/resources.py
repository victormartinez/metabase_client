from urllib.parse import urljoin

import requests


class Resource:

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def authenticated(self, method, path, token, **kwargs):
        headers = {"Content-Type": "application/json", "X-Metabase-Session": token}
        return self.request(method, path, headers=headers, **kwargs)

    def request(self, method, path, **kwargs):
        url = urljoin(self.endpoint, path)
        return requests.request(method, url, **kwargs)


class SessionResource(Resource):

    PATH_LOGIN = "/api/session"

    def get_token(self, username, password):
        headers = {"Content-Type": "application/json"}
        auth_data = {"username": username, "password": password}
        response = self.request(
            "post", self.PATH_LOGIN, headers=headers, json=auth_data
        )
        return response.json().get("id")


class CardResource(Resource):

    PATH_LIST_CARDS = "/api/card"

    def list(self, auth_token):
        response = self.authenticated(
            "get", self.PATH_LIST_CARDS, auth_token
        )
        return response.json()
