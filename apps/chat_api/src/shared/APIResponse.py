from flask import make_response
from enum import Enum
from flask import jsonify


class APIResponseCode(Enum):

    SUCCESS = 0
    INVALID_DATA = 1
    INVALID_CREDENTIALS = 2


class APIResponse:

    def __init__(self,
                 api_code: APIResponseCode,
                 content: dict = {},
                 message: str = None,
                 content_type: str = "application/json",
                 status_code: int = 200):
        self.api_code = api_code
        self.content = content
        self.message = message
        self.content_type = content_type
        self.status_code = status_code
        self.headers = {}

    def raw_response(self):
        result = {
            'status': self.api_code.value,
            'data': self.content,
            'message': self.message
        }

        response = make_response(jsonify(result), self.status_code)
        response.headers['Content-Type'] = self.content_type
        for key in self.headers:
            response.headers[key] = self.headers[key]
        return response
