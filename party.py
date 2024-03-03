from types import List
from party_members import PartyMember, AttendanceStatus

class Party:
    def __init__(self) -> None:
        self._name: str
        self._members: List[PartyMember]

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def


class Contact:
    pass


class Address:
    pass


class Gift:
    pass


class Phone:
    pass


class Email:
    pass
