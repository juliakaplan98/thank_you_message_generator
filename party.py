from types import List
from party_members import PartyMember, AttendanceStatus
from email import Email
from phone import Phone
from gift import Gift


class Party:
    def __init__(self) -> None:
        self._name: str
        self._members: List[PartyMember]
        self._email: Email
        self._phone: Phone
        self._gift: Gift

    # Properties
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

    @property
    def phone(self) -> Phone:
        return self._phone

    @phone.setter
    def phone(self, phone: Phone) -> None:
        self._phone = phone

    @property
    def email(self) -> Email:
        return self._email

    @email.setter
    def email(self, email: Email) -> None:
        self._email = email

    @property
    def gift(self) -> Gift:
        return self._gift

    @email.setter
    def email(self, gift: Gift) -> None:
        self._gift = gift

    # members
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
