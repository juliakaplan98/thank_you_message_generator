import json
import os
from party.party import Party
from party.phone import Phone, PhoneType
from party.pemail import Email, EmailType
from party.address import Address, AddressType
from party.gift import Gift, GiftType
from party.party_members import PartyMember, AttendanceStatus

if __name__ == '__main__':
    p = Party('Kaplan')
    p.phone = Phone('555.222.1212', PhoneType.Cell)
    p.email = Email('test@.msn.com', EmailType.NA)
    p.address = Address(
        type=AddressType.Home,
        address0='6421 Booth Str',
        address1='Apt 6D',
        city='Rego PArk',
        state='NY',
        zip=11374)
    p.gift = Gift(type=GiftType.Cash, amount=500)
    p.members.extend([
        PartyMember(name='Natalya Kaplan', attendance=AttendanceStatus.Yes),
        PartyMember(name='Michael Kaplan', attendance=AttendanceStatus.Yes),
        PartyMember(name='Minnie Kaplan', attendance=AttendanceStatus.Yes),
    ])

    wd = os.getcwd()
    path = os.path.join(wd, 'data', 'test.json')
    with open(path, 'w') as file:
        json.dump(p.jsonEncode(), file)

    with open(path, 'r') as file:
        pp = json.load(file)
        ppp = Party.jsonDecode(pp)
        print(ppp)
