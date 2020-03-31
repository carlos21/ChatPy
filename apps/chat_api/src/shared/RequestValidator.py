import json
from cerberus import Validator
from werkzeug.wrappers import Request
from apps.chat_api.src.shared.InvalidRequestException import InvalidRequestException
from munch import Munch


class RequestValidator:

    def __init__(self, request: Request, validation_schema: object):
        self.request = request
        self.validator = Validator()
        self.validator.schema = validation_schema

    def validate(self) -> object:
        try:
            data_string = self.request.data.decode('utf-8')
            decoded_object = json.loads(data_string)
            if self.validator.validate(decoded_object):
                return Munch(decoded_object)
            else:
                raise InvalidRequestException

        except json.decoder.JSONDecodeError:
            raise InvalidRequestException
