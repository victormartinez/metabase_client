class Resource:
    def __init__(self, http_client):
        self.http_client = http_client


class SessionResource(Resource):

    PATH_LOGIN = "/api/session"

    def get_token(self, username, password):
        headers = {"Content-Type": "application/json"}
        auth_data = {"username": username, "password": password}
        response = self.http_client.request(
            "post", self.PATH_LOGIN, headers=headers, json=auth_data
        )
        return response.json().get("id")


class CardResource(Resource):

    PATH_LIST_CARDS = "/api/card"

    def list(self, auth_token):
        response = self.http_client.authenticated(
            "get", self.PATH_LIST_CARDS, auth_token
        )
        return response.json()
