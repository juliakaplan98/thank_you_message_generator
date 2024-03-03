from enum import Enum


def PhoneType(Enum):
    Cell = 0
    Home = 1
    Office = 2


class Phone:
    def __init__(self) -> None:
        self._type: PhoneType
        self._phone: str

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone) -> None:
        self._phone = phone

    @property
    def type(self) -> PhoneType:
        return self._type

    @type.setter
    def type(self, type: PhoneType) -> None:
        self._type = type
