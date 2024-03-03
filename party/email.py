from enum import Enum


class EmailType(Enum):
    Home = 0
    Office = 1


class Email:
    def __init__(self) -> None:
        self._type: EmailType
        self._Email: str

    # Properties
    @property
    def email(self) -> str:
        return self._Email

    @email.setter
    def email(self, email) -> None:
        if self.validateEmail(email):
            self._Email = email

    @property
    def type(self) -> EmailType:
        return self._type

    @type.setter
    def type(self, type: EmailType) -> None:
        self._type = type

    def validateEmail(self, email) -> bool:
        return True
