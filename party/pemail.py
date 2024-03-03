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
            "email": self.email,
            "type": self.type.name
        }

    def jsonDecode(self, pemail: dict[str, Any]) -> None:
        self.email = pemail.get('email')
        self.type = pemail.get('type')
