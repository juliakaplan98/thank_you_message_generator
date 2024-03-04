from enum import Enum
from typing import Any


class PhoneType(Enum):
    NA = 0
    Cell = 1
    Home = 2
    Office = 3


class Phone:
    def __init__(
            self,
            phone: str = '',
            type: PhoneType = PhoneType.NA) -> None:
        self._type: PhoneType = type
        self._phone: str = phone

    # Properties
    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone) -> None:
        if self.validatePhone(phone):
            self._phone = phone

    @property
    def type(self) -> PhoneType:
        return self._type

    @type.setter
    def type(self, type: PhoneType) -> None:
        self._type = type

    def validatePhone(self, phone) -> bool:
        # TODO validate phone number for usa
        return True

    def jsonEncode(self) -> dict[str, Any]:
        return {
            'phone': self.phone,
            'type': self.type.name
        }

    @staticmethod
    def jsonDecode(phone: dict[str, Any]):
        return Phone(
            phone=phone.get('phone'),
            type=phone.get('type'))
