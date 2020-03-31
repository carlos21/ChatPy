from pymongo import MongoClient


class MongoRepository:

    @property
    def client(self):
        return self._client

    @property
    def db(self):
        return self._client['chatpy']

    def __init__(self, client: MongoClient):
        self._client = client

