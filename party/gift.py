from enum import Enum
from typing import Any


class GiftType(Enum):
    NA = 0
    Cash = 1
    Present = 2


class Gift:
    def __init__(
            self,
            type: GiftType = GiftType.NA,
            description: str = '',
            amount: int = 0) -> None:
        self._type: GiftType = type
        self._description: str = description
        self._amount: int = amount

    # Properties
    @property
    def type(self) -> GiftType:
        return self._type

    @type.setter
    def type(self, type: GiftType) -> None:
        self._type = type

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        self._description = description

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, amount: int) -> None:
        self._amount = amount

    def jsonEncode(self) -> dict[str, Any]:
        return {
            "description": self.description,
            "type": self.type.name,
            "amount": self.amount
        }

    def jsonDecode(self, gift: dict[str, Any]) -> None:
        self.description = dict.get('description')
        self.type = dict.get('type')
        self.amount = dict.get('amount')
