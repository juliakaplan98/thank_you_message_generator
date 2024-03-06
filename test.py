import json
import os
from party.party import Party
from party.phone import Phone, PhoneType
from party.pemail import Email, EmailType
from party.address import Address, AddressType
from party.gift import Gift, GiftType
from party.party_members import PartyMember, AttendanceStatus
from occasion import Occasion, OccasionType

if __name__ == '__main__':
    p0 = Party('Kaplan')
    p0.phone = Phone('555.222.1212', PhoneType.Cell)
    p0.email = Email('test@.msn.com', EmailType.NA)
    p0.address = Address(
        type=AddressType.Home,
        address0='6421 Booth Str',
        address1='Apt 6D',
        city='Rego PArk',
        state='NY',
        zip=11374)
    p0.gift = Gift(type=GiftType.Cash, amount=500)
    p0.members.extend([
        PartyMember(name='Natalya Kaplan', attendance=AttendanceStatus.Yes),
        PartyMember(name='Michael Kaplan', attendance=AttendanceStatus.Yes),
        PartyMember(name='Minnie Kaplan', attendance=AttendanceStatus.Yes),
    ])

    p1 = Party('Kurgan')
    p1.phone = Phone('555.222.1212', PhoneType.Cell)
    p1.email = Email('test@.msn.com', EmailType.NA)
    p1.address = Address(
        type=AddressType.Home,
        address0='6421 Booth Str',
        address1='Apt 6D',
        city='Boca Raton',
        state='FL',
        zip=11374)
    p1.gift = Gift(type=GiftType.Cash, amount=500)
    p1.members.extend([
        PartyMember(name='Alex Kurgan', attendance=AttendanceStatus.Yes),
        PartyMember(name='Simona Kurgan', attendance=AttendanceStatus.Yes),
    ])

    occasion = Occasion(name='Julia and Michael wedding',
                        type=OccasionType.WEDDING)
    occasion.addParty(p0)
    occasion.addParty(p1)

    Occasion.dumpOccasionOnFile(occasion=occasion)

    occ = Occasion.loadOccasionFromFile(occasion.name)

    print(occ)
