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
    def members(self) -> List[PartyMember]:
        return self._members

    @members.setter
    def members(self, members: List[PartyMember]) -> None:
        self._members = members

    def getMembersList(self) -> List[str]:
        members = [m.name for m in self._members]
        members.sort()
        return members

    def getAttendeesList(self) -> List[str]:
        members = [m.name for m in self._members if m.attendance ==
                   AttendanceStatus.Yes]
        members.sort()
        return members

    def getNoAttendeesList(self) -> List[str]:
        members = [m.name for m in self._members if m.attendance ==
                   AttendanceStatus.No]
        members.sort()
        return members


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
