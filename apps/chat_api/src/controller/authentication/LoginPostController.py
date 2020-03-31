from werkzeug.wrappers import Request
from apps.chat_api.src.shared.ValidatableController import ValidatableController
from apps.chat_api.src.shared.RequestValidator import RequestValidator
from apps.chat_api.src.shared.InvalidRequestException import InvalidRequestException
from apps.chat_api.src.shared.APIResponse import APIResponse, APIResponseCode
from src.chat_api.authentication.application.LoginUseCase import LoginUseCase
from src.chat_api.authentication.application.LoginUserRequest import LoginUserRequest
from src.shared.domain.valueobject.Exceptions import InvalidPasswordException


class LoginPostController(ValidatableController):

    schema = {
        'username': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'required': True}
    }

    def __init__(self, usecase: LoginUseCase):
        self.usecase = usecase

    def invoke(self, request: Request):
        validator = RequestValidator(request, self.schema)
        data = validator.validate()

        login_user_request = LoginUserRequest(username=data.username, password=data.password)

        response = APIResponse(api_code=APIResponseCode.INVALID_CREDENTIALS)

        if self.usecase.login(login_user_request) is not None:
            # TODO
            response = APIResponse(api_code=APIResponseCode.SUCCESS, content={'token': '123456'})

        return response.raw_response()
