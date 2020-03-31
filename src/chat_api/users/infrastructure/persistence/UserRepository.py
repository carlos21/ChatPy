from abc import ABCMeta, abstractmethod
from src.chat_api.users.domain.valueobjects.UserPassword import UserPassword


class UserRepository(metaclass=ABCMeta):

    @abstractmethod
    def search_by_username_and_password(self, username: str, password: UserPassword):
        pass
