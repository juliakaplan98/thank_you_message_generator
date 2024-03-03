import json
from enum import Enum
from typing import Any


class EmailType(Enum):
    Home = 0
    Office = 1


class Email:
    def __init__(self) -> None:
        self._type: EmailType
        self._email: str

    # Properties
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email) -> None:
        if self.validateEmail(email):
            self._email = email

    @property
    def type(self) -> EmailType:
        return self._type

    @type.setter
    def type(self, type: EmailType) -> None:
        self._type = type

    def validateEmail(self, email) -> bool:
        return True

    def jsonEncode(self) -> dict[str, Any]:
        return {
            "email": self._email,
            "type": self._type.name
        }

    def jsonDecode(self, string: str) -> None:
        jsonStr = json.loads(string)
        self.email = jsonStr.get('email')
        self.type = jsonStr.get('type')


if __name__ == '__main__':
    email = Email()

    let = '{"email": "test@msn.com", "type": "222-555-1212"}'
    email.jsonDecode(let)

    print(email.email)
    print(email.type)
