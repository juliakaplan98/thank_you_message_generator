import os
import json
from typing import List, Any
from enum import Enum
from party.party import Party
from party.address import Address


class OccasionType(Enum):
    NA = 0
    WEDDING = 1


class Occasion:
    def __init__(
            self,
            name: str = '',
            type: OccasionType = OccasionType.NA,
            address: Address = Address(),
            parties: List[Party] = None) -> None:
        self._name: str = name
        self._address: Address = address,
        self._type: OccasionType = type
        # TODO: Add date of event
        if parties is None:
            parties = []
        self._parties: List[Party] = parties

    @property
    def type(self) -> OccasionType:
        return self._type

    @type.setter
    def type(self, type: Address) -> None:
        self._type = type

    @property
    def address(self) -> Address:
        return self._address

    @address.setter
    def address(self, address: Address) -> None:
        self._address = address

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def parties(self) -> List[Party]:
        """ Return tuple to prevent adding party without checking """
        return self._parties

    @parties.setter
    def parties(self, parties: List[Party]) -> None:
        self._parties = parties

    # TODO add getter and setter for occasion type

    # TODO add getter and setter for occasion

    # TODO add setter and getter for date of occasion

    def addParty(self, party: Party) -> bool:
        """ Add Party by name"""
        # Check if party name is exist
        if len([p for p in self._parties if p.name == party.name]) != 0:
            return False
        self._parties.append(party)
        return True

    def removeParty(self, name: str) -> bool:
        """ Remove Party by name"""
        if len(self._parties) == 0:
            return False
        count = len(self._parties)
        self._parties = [
            party for party in self._parties if party.name != name]
        return count != len(self._parties)

    def jsonEncode(self) -> dict[str, Any]:
        return {
            'name': self.name,
            # 'address': self.address.jsonEncode(),
            'type': self.type.name,
            'parties': [parties.jsonEncode() for parties in self.parties],
        }

    @staticmethod
    def jsonDecode(occasion: dict[str, any]):
        return Occasion(
            name=occasion.get('name'),
            #  address=Address.jsonDecode(occasion.get('address')),
            type=occasion.get('type'),
            parties=[Party.jsonDecode(party)
                     for party in occasion.get('parties')],
        )

    @staticmethod
    def saveOccasionOnFile(occasion: dict[str, Any]) -> bool:
        fileName = occasion.get(occasion.name)
        if not fileName:
            return False
        workingDirectory = os.getcwd()
        dataPath = os.path.join(workingDirectory, 'data')
        if not os.path.exists(dataPath):
            os.makedirs(os.path.join(dataPath))
        path = os.path.join(dataPath, f'{occasion.name}.json')
        with open(path, 'w') as file:
            json.dump(occasion.jsonEncode(), file)
