class StringValueObject:

    @property
    def value(self):
        return self._value

    def __init__(self, value: str):
        self._value = value
