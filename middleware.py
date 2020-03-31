from werkzeug.wrappers import Request, Response, ResponseStream
import json


class Middleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # request = Request(environ)
        return self.app(environ, start_response)

        # try:
        #     data_string = request.data.decode('utf-8')
        #     decoded_object = json.loads(data_string)
        #     return self.app(environ, start_response)
        # except json.decoder.JSONDecodeError:
        #     result = {'error': 'Invalid json'}
        #     res = Response(result, mimetype='application/json', status=400)
        #     return res(environ, start_response)
