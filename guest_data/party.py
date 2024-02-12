import pandas as pd

class Group:
    def __init__(self, address, email, phone, gift):
        self.guest_names = []
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



# Get number of guest per group
group_size = int(input("Number of guests in this group? ")) 
# Get information about group
group_address = input("Party's Address: ")
group_email = input("Party's Email: ")
group_phone = input("Party's Phone Number: ")
group_gift = input("Gift Received: ")

# Create group    
group1 = Group(group_address, group_email, group_phone, group_gift)

# Add names of guests to group


count=0
for i in range(0,group_size):
    count+=1
    guest_name = input(f"{count}. Guest's First and Last Name: ")
    group1.add_guest(guest_name)
    guest_attendance = input(f"Did {guest_name} attend the event? ")
    group1.add_attendance(guest_attendance)

# Access stored data
guest_names = group1.get_guest()
attendance = group1.get_attendance()


# data for dataframe
data = {'Party Members': group1.guest_names,
        'Address': group1.address,
        'Email': group1.email,
        'Phone Number': group1.phone,
        'Attendance Status': group1.attendance,
        'Gift': group1.gift}


# Creates pandas DataFrame.
df = pd.DataFrame(data)
print(df)