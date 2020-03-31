from flask import Flask, jsonify


class HealthCheckGetController:

    def __init__(self):
        pass

    def invoke(self):
        return jsonify({'status': 'ok'})
