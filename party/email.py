import json
from typing import Any
from enum import Enum


class EmailType(Enum):
    Home = 0
    Office = 1


class Email:
    def __init__(self) -> None:
        self._type: EmailType
        self._email: str

    # Properties
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email) -> None:
        if self.validateEmail(email):
            self._email = email

    @property
    def type(self) -> EmailType:
        return self._type

    @type.setter
    def type(self, type: EmailType) -> None:
        self._type = type

    def validateEmail(self, email) -> bool:
        return True

    def jsonEncode(self) -> dict[str, Any]:
        return {
            "email": self._email,
            "type": self._type.value
        }

    def jsonDecode(self, string: str) -> None:
        try:
            jsonStr = json.loads(string)
            self._email = jsonStr.email
        except:
            print('Error')
