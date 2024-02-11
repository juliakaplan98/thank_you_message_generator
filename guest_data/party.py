# class Party:
#     def __init__(self, member_name, address, email, phone, attendance, gift):
#         self.member_name = member_name
#         self.member_list = [] # Initialize an empty list to store all member names
#         self.address = address
#         self.email = email
#         self.phone = phone
#         self.attendance = attendance
#         self.gift = gift

# class Member:
#     def __init__(self, member_name, attendance):
#         self.member_name = member_name
#         self.attendance = attendance
#         self.member_status_list = [] # Initialize an empty list to store all member names

#     def add_member(self, member):
#         self.member_status_list.append(member)
    
#     def get_members(self):
#         return self.member_status_list

# # Create member    
# party_member = Member("Julia Kaplan", "Yes")
# # Add member to party
# party_member.add_member(party_member)
# # Access all members in the party
# member_list = party_member.get_members()
# print(member_list[0].member_name)


class Party:
    def __init__(self, party_id, address, email, phone, gift):
        self.party_id = party_id
        self.guest_names = []
        self.address = address
        self.email = email
        self.phone = phone
        self.gift = gift
        # self.attendance = attendance

    def add_guest(self, guest):
        self.guest_names.append(guest)
    
    def get_guest(self):
        return self.guest_names

# Create party    
party_1 = Party("X Family", "xx-xx Madison Ave, Apt xx, Manhattan, NY, xxxxx", "xxx123@gmail.com", "(xxx) xxx-xxxx", "Michael Aram Photo Frame")
# Add member to party
guest_1 = party_1.add_guest("John X")
guest_2 = party_1.add_guest("Ann X")

# Access all members in the party
guest_names = party_1.get_guest()
print(f'Party: {party_1.party_id}\nGuest in Party: {party_1.guest_names}\n\nContact Information\n-------------------\nAddress: {party_1.address}\nEmail: {party_1.email}\nPhone: {party_1.phone}\n\nGift Received: {party_1.gift}')