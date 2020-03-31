from src.shared.domain.valueobject.StringValueObject import StringValueObject
from src.shared.domain.valueobject.Exceptions import InvalidPasswordException
import re
import hashlib


class UserPassword(StringValueObject):

    def __init__(self, value: str):
        super().__init__(value)
        self.ensure_is_valid()

    def ensure_is_valid(self):
        if not re.compile(r'(\w{8,})').findall(self.value):
            raise InvalidPasswordException

        elif not re.compile(r'[a-z]+').findall(self.value):
            raise InvalidPasswordException

        elif not re.compile(r'[A-Z]+').findall(self.value):
            raise InvalidPasswordException

        elif not re.compile(r'[0-9]+').findall(self.value):
            raise InvalidPasswordException

    def encrypted(self):
        return hashlib.sha256(self.value.encode()).hexdigest()
