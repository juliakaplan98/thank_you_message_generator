from enum import Enum


class GiftType(Enum):
    Cash = 0
    Present = 1


class Gift:
    def __init__(self) -> None:
        self._type: GiftType
        self._description: str
        self._amount: int

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
        return self._type

    @amount.setter
    def amount(self, amount: int) -> None:
        self._amount = amount
