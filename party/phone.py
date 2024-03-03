import json
from enum import Enum
from typing import Any


class PhoneType(Enum):
    Cell = 0
    Home = 1
    Office = 2


class Phone:
    def __init__(self) -> None:
        self._type: PhoneType
        self._phone: str

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
        return True

    def jsonEncode(self) -> dict[str, Any]:
        return {
            "phone": self.phone,
            "type": self.type.name
        }

    def jsonDecode(self, string: str) -> None:
        jsonStr = json.loads(string)
        self.phone = jsonStr.get('phone')
        self.type = jsonStr.get('type')
