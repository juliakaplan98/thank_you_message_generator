from enum import Enum
from typing import Any


class AttendanceStatus(Enum):
    NA = 0
    Yes = 1
    No = 2


class PartyMember:
    def __init__(
            self,
            name: str = '',
            attendance: AttendanceStatus = AttendanceStatus.NA) -> None:
        self._name: str = name
        self._attendance: AttendanceStatus = attendance

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def attendance(self) -> AttendanceStatus:
        return self._attendance

    @attendance.setter
    def attendance(self, attendance: AttendanceStatus) -> None:
        self._attendance = attendance

    def jsonEncode(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "attendance": self.attendance.name
        }

    @staticmethod
    def jsonDecode(member: dict[str, Any]):
        return PartyMember(
            name=member.get('name'),
            attendance=member.get('attendance'))
