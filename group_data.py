import pandas as pd
from pathlib import Path
import uuid
import os
import csv

class GroupData:
    def __init__(self, id, address, email, phone, gift):
        self.guest_names = []
        self.id = id
        self.address = address
        self.email = email
        self.phone = phone
        self.attendance = []
        self.gift = gift 
    def add_guest(self, guest):
        self.guest_names.append(guest) 
    def get_guest(self):
        return self.guest_names
    def add_attendance(self, attendance):
        self.attendance.append(attendance) 
    def get_attendance(self):
        return self.attendance

# # Group identification number
# group_id = uuid.uuid4()

# # Get number of guest per group
# group_size = int(input("Number of guests in this group? ")) 
# # Get information about group
# group_address = input("\nParty's Address: ")
# group_email = input("Party's Email: ")
# group_phone = input("Party's Phone Number: ")
# group_gift = input("Gift Received: ")

# # Create group    
# new_group = GroupData(group_id, group_address, group_email, group_phone, group_gift)

# # Add names of guests to group
# count=0
# for i in range(0,group_size):
#     count+=1
#     guest_name = input(f"\n{count}. Guest's First and Last Name: ")
#     new_group.add_guest(guest_name)
#     guest_attendance = input(f"Did {guest_name} attend the event (Y/N)? ")
#     new_group.add_attendance(guest_attendance)

# # Access stored data
# guest_names = new_group.get_guest()
# attendance = new_group.get_attendance()


# # data for dataframe
# data = {'ID': new_group.id,
#         'Party Members': new_group.guest_names,
#         'Address': new_group.address,
#         'Email': new_group.email,
#         'Phone Number': new_group.phone,
#         'Attendance Status': new_group.attendance,
#         'Gift': new_group.gift}

# df = pd.DataFrame(data, columns=['ID', 'Party Members', 'Address', 'Email', 'Phone Number', 'Attendance Status', 'Gift'])
# path = Path('GuestList.csv')

# if path.is_file() == False:
#     with open('GuestList.csv', 'w') as csvFile:
#         df.to_csv('GuestList.csv', index=False,header=True)
#         csvFile.close()
#         print("CSV file created successfully.")

# else:
#     df.to_csv('GuestList.csv', mode='a', index=False, header=False)
#     print("Data appended successfully.")

