from typing import Any
from enum import Enum


class EmailType(Enum):
    NA = 0
    Home = 1
    Office = 2


class Email:
    def __init__(
            self,
            email: str = '',
            type: EmailType = EmailType.NA) -> None:
        self._type: EmailType = type
        self._email: str = email

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
            'email': self.email,
            'type': self.type.name
        }

    @staticmethod
    def jsonDecode(pemail: dict[str, Any]):
        return Email(
            email=pemail.get('email'),
            type=pemail.get('type'))
