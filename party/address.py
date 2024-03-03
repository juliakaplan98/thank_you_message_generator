from enum import Enum
from typing import Any


class AddressType(Enum):
    NA = 0
    Home = 1
    Office = 2


class Address:
    def __init__(
            self,
            address0: str = '',
            address1: str = '',
            city: str = '',
            state: str = '',
            zip: int = 0,
            type: AddressType = AddressType.NA) -> None:
        self._address0: str = address0
        self._address1: str = address1
        self._city: str = city
        self._state: str = state
        self._zip: int = zip
        self._type = type

    # Properties
    @property
    def type(self) -> AddressType:
        return self._type

    @type.setter
    def type(self, type: AddressType) -> None:
        self._type = type

    @property
    def address0(self) -> str:
        return self._address0

    @address0.setter
    def address0(self, address: str) -> None:
        self._address0 = address

    @property
    def address1(self) -> str:
        return self._address1

    @address1.setter
    def address1(self, address: str) -> None:
        self._address1 = address

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, city: str) -> None:
        self._city = city

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        self._state = state

    @property
    def zip(self) -> int:
        return self._zip

    @zip.setter
    def zip(self, zip: int) -> None:
        self._zip = zip

    def jsonEncode(self) -> dict[str, Any]:
        return {
            'address0': self.address0,
            'address1': self.address1,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,
            'type': self.type.name
        }

    def jsonDecode(self, address: dict[str, Any]) -> None:
        self.address0 = address.get('address0')
        self.address1 = address.get('address1')
        self.city = address.get('city')
        self.state = address.get('state')
        self.zip = address.get('zip')
        self.type = address.get('type')
