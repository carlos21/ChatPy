from src.chat_api.authentication.domain.UserId import UserId


class User:

    def __init__(self, identifier: UserId, username: str, password: str):
        self.identifier = identifier
        self.username = username
        self.password = password
