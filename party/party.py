import json
from types import Any
from party_members import PartyMember, AttendanceStatus
from pemail import Email
from phone import Phone
from gift import Gift
from address import Address


class Party:
    def __init__(self) -> None:
        self._name: str
        self._members: list[PartyMember]
        self._email: Email
        self._phone: Phone
        self._gift: Gift
        self._address: Address

    def jsonEncode(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "members": [member.jsonEncode() for member in self.members],
            "email": self.email.jsonEncode(),
            "phone": self.phone.jsonEncode(),
            "gift": self.gift.jsonEncode(),
            "address": self.jsonEncode(),
        }

    def jsonDecode(self, string: str) -> None:
        jsonStr = json.loads(string)
        self.name = jsonStr.get('name')
        self.email = self.email.jsonDecode(jsonStr.get('email'))
        self.phone = self.phone.jsonDecode(jsonStr.get('phone'))
        self.gift = self.gift.gift.jsonDecode(jsonStr.get('gift'))
        self.address = self.address.jsonDecode(jsonStr.get('address'))

        self.members = []
        for m in jsonStr.get('members'):
            member = PartyMember()
            self.members.append(member.jsonDecode(m))

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

    @email.setter
    def email(self, gift: Gift) -> None:
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
