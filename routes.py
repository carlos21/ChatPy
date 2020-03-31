# from app import app
from apps.chat_api.src.controller.health_check.HealthCheckGetController import HealthCheckGetController
from apps.chat_api.src.controller.authentication.LoginPostController import LoginPostController
from src.chat_api.users.infrastructure.persistence.MongoUserRepository import MongoUserRepository
from src.chat_api.authentication.application.LoginUseCase import LoginUseCase
from flask import request, Flask
from middleware import Middleware
from pymongo import MongoClient
from apps.chat_api.src.shared.APIResponse import APIResponse, APIResponseCode
from apps.chat_api.src.shared.InvalidRequestException import InvalidRequestException
from src.shared.domain.valueobject.Exceptions import InvalidPasswordException


app = Flask(__name__)
app.wsgi_app = Middleware(app.wsgi_app)

client = MongoClient('mongodb', 27017, username='chatpy-user', password='secret', authSource='chatpy')


@app.errorhandler(InvalidPasswordException)
def handle_exception(e):
    response = APIResponse(api_code=APIResponseCode.INVALID_CREDENTIALS,
                           message="Handling InvalidPasswordException xd")
    return response.raw_response()


@app.errorhandler(InvalidRequestException)
def handle_exception(e):
    response = APIResponse(api_code=APIResponseCode.INVALID_DATA,
                           message="Handling InvalidRequestException xd")
    return response.raw_response()


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/health-check')
def health_check():
    controller = HealthCheckGetController()
    return controller.invoke()


@app.route('/authentication', methods=['POST'])
def authentication():
    repository = MongoUserRepository(client)
    login_usecase = LoginUseCase(repository)
    controller = LoginPostController(login_usecase)
    return controller.invoke(request)


if __name__ == "__main__":
    app.run(debug=True)
