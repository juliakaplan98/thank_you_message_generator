from enum import Enum


class AddressType(Enum):
    Home = 0
    Office = 1


class Address:
    def __init__(self) -> None:
        self._address0: str
        self._address1: str
        self._city: str
        self._state: str
        self._zip: int

    # Properties
    @property
    def address0(self) -> str:
        return self._address0

    @address0.setter
    def address0(self, address) -> None:
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
