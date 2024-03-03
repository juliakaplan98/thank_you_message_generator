from enum import Enum


class AttendanceStatus(Enum):
    Yes = 0
    No = 1


class PartyMember:
    def __init__(self) -> None:
        self._name: str
        self._attendance: AttendanceStatus

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
