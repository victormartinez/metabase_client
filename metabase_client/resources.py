from typing import Dict


class Resource:
    def __init__(self, client):
        self.client = client


class SessionResource(Resource):

    PATH_LOGIN = "/api/session"

    def get_token(self, username: str, password: str):
        headers = {"Content-Type": "application/json"}
        auth_data = {"username": username, "password": password}
        response = self.client.request(
            "post", self.PATH_LOGIN, headers=headers, json=auth_data
        )
        return response.json().get("id")


class CardResource(Resource):

    PATH_LIST_CARDS = "/api/card"
    URL_POST_CARD_ID = "/api/card/{}/query"
    URL_POST_CARD_ID_EXPORT = "/api/card/{}/query/{}"

    def list(self, auth_token: str):
        response = self.client.authenticated("get", self.PATH_LIST_CARDS, auth_token)
        return response.json()

    def execute(self, card_number: int, data: Dict = None, export: str = None):
        if export:
            path = self.URL_POST_CARD_ID_EXPORT.format(card_number, export)
        else:
            path = self.URL_POST_CARD_ID.format(card_number)

        response = self.client.authenticated(
            "post", self.endpoint, path, self.token, json=data
        )
        return response.json()
