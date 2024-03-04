import json
from typing import Any, List
from .phone import Phone
from .gift import Gift
from .address import Address
from .pemail import Email
from .party_members import PartyMember, AttendanceStatus


class Party:
    def __init__(
            self,
            name: str = '',
            email: Email = Email(),
            phone: Phone = Phone(),
            gift: Gift = Gift(),
            address: Address = Address(),
            members: List[PartyMember] = None
    ) -> None:
        self._name: str = name
        if members is None:
            members = []
        self._members: list[PartyMember] = members
        self._email: Email = email
        self._phone: Phone = phone
        self._gift: Gift = gift
        self._address: Address = address

    # Properties
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def members(self) -> list[PartyMember]:
        return self._members

    @members.setter
    def members(self, members: list[PartyMember]) -> None:
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

    @gift.setter
    def gift(self, gift: Gift) -> None:
        self._gift = gift

    @property
    def address(self) -> Address:
        return self._address

    @address.setter
    def address(self, address: Address) -> None:
        self._address = address

    # members
    def getMembersList(self) -> list[str]:
        members = [m.name for m in self._members]
        members.sort()
        return members

    def getAttendeesList(self) -> list[str]:
        members = [m.name for m in self._members if m.attendance ==
                   AttendanceStatus.Yes]
        members.sort()
        return members

    def getNoAttendeesList(self) -> list[str]:
        members = [m.name for m in self._members if m.attendance ==
                   AttendanceStatus.No]
        members.sort()
        return members

    # Methods
    def jsonEncode(self) -> dict[str, Any]:
        return {
            'name': self.name,
            'members': [member.jsonEncode() for member in self.members],
            'email': self.email.jsonEncode(),
            'phone': self.phone.jsonEncode(),
            'gift': self.gift.jsonEncode(),
            'address': self.address.jsonEncode(),
        }

    @staticmethod
    def jsonDecode(party: dict[str, any]):
        return Party(
            name=party.get('name'),
            email=Email.jsonDecode(party.get('email')),
            phone=Phone.jsonDecode(party.get('phone')),
            gift=Gift.jsonDecode(party.get('gift')),
            address=Address.jsonDecode(party.get('address')),
            members=[PartyMember(
                name=member.get('name'), attendance=member.get('attendance'))
                for member in party.get('members')]
        )
