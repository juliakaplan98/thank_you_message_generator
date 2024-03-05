from typing import List
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
            parties: List[Party] = None) -> None:
        self._name: str = name
        self._address: Address
        self._type: OccasionType = type
        # TODO: Add date of event
        if parties is None:
            parties = []
        self._parties: List[Party] = parties

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def parties(self) -> tuple[Party]:
        """ Return tuple to prevent adding party without checking """
        return tuple(self._parties)

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
