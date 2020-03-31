import uuid


class UUID:

    @property
    def value(self):
        self._value

    def __init__(self, value: str):
        self.ensure_is_valid(value)
        self._value = value

    def ensure_is_valid(self, value: str):
        pass

    @classmethod
    def random(cls):
        return uuid.uuid4()
