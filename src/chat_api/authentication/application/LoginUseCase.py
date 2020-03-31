from src.chat_api.authentication.application.LoginUserRequest import LoginUserRequest
from src.chat_api.users.infrastructure.persistence.UserRepository import UserRepository
from src.chat_api.users.domain.valueobjects.UserPassword import UserPassword


class LoginUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def login(self, request: LoginUserRequest):
        password = UserPassword(request.password)
        return self.repository.search_by_username_and_password(request.username, password)
