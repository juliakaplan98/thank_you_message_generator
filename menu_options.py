import pandas as pd
from pathlib import Path
import uuid
import os
# import csv
import json
from group_data import GroupData

def main_menu():
    print("\n\tMain Menu")
    print("\t---------\n")
    print("\t(1) Edit Wedding Guest Contact Information")
    print("\t(2) Generate Thank You Message for Wedding Guests")
    print("\t(E) Exist")

def show_guest_menu():
    print("\n\tWedding Guest Contact Information Menu")
    print("\t--------------------------------------\n")
    print("\t(1) Create a New Group")
    print("\t(2) Add Guest to Existing Group")
    print("\t(3) Remove Guest from Existing Group")
    print("\t(4) Remove Existing Group")
    print("\t(5) Show All Existing Guests")
    print("\t(6) Return to Main Menu")
    print("\t(E) Exist")

def show_message_menu():
    print("\tWedding Thank You Message Generator")
    print("\t--------------------------------------\n")
    print("\n\t(1) Generate Thank You Message for individual Guest")
    print("\t(2) Generate Thank You Message for Group")
    print("\t(3) Return to Main Menu")
    print("\t(E) Exist")


def menu():
    while True:
        main_menu()
        choice = input("\nSelect Option from Menu: ").lower()

        if choice == '1':
            #####################################################
            show_guest_menu()
            choice = input("\nSelect Option from Menu: ").lower()
            if choice == '1':
                # Group identification number
                group_id = uuid.uuid4()
                # Get number of guest per group
                group_size = int(input("Number of guests in this group? ")) 
                # Get information about group
                group_address = input("\nParty's Address: ")
                group_email = input("Party's Email: ")
                group_phone = input("Party's Phone Number: ")
                group_gift = input("Gift Received: ")
                # Create group    
                new_group = GroupData(group_id, group_address, group_email, group_phone, group_gift)

                # Add names of guests to group
                count=0
                for i in range(0,group_size):
                    count+=1
                    guest_name = input(f"\n{count}. Guest's First and Last Name: ")
                    new_group.add_guest(guest_name)
                    guest_attendance = input(f"Did {guest_name} attend the event (Y/N)? ")
                    new_group.add_attendance(guest_attendance)

                # Access stored data
                guest_names = new_group.get_guest()
                attendance = new_group.get_attendance()

                # data for dataframe

                # 'ID': new_group.id,
                data = {
                        'Party Members': new_group.guest_names,
                        'Address': new_group.address,
                        'Email': new_group.email,
                        'Phone Number': new_group.phone,
                        'Attendance Status': new_group.attendance,
                        'Gift': new_group.gift}

                df = pd.DataFrame(data, columns=['ID', 'Party Members', 'Address', 'Email', 'Phone Number', 'Attendance Status', 'Gift'])
                # path = Path('GuestList.csv')

                # if path.is_file() == False:
                #     with open('GuestList.csv', 'w') as csvFile:
                #         df.to_csv('GuestList.csv', index=False,header=True)
                #         csvFile.close()
                #         print("CSV file created successfully.")
                # else:
                #     df.to_csv('GuestList.csv', mode='a', index=False, header=False)
                #     print("Data appended successfully.")

                # create prepare data for json file
                with open('data.json', 'w') as f:
                    json.dump(data, f)



                ##########################################################        
            elif choice == '2':
                print("\nMenu Option in Progress.")
            elif choice == '3':
                main_menu()
            elif choice == 'e':
                return
            else:
                print(f'\nIncorrect menu option selected: {choice}. Please select an option from the menu.')
        elif choice == '2':
            show_message_menu()
            choice = input("\nSelect Option from Menu: ").lower()
            if choice == '1':
                print("\nMenu Option in Progress.")
            elif choice == '2':
                print("\nMenu Option in Progress.")
            elif choice == '3':
                print("\nMenu Option in Progress.")
            elif choice == '4':
                print("\nMenu Option in Progress.")
            elif choice == '5':
                print("\nMenu Option in Progress.")
            elif choice == '6':
                main_menu()
            elif choice == 'e':
                return
            else:
                print(f'\nIncorrect menu option selected: {choice}. Please select an option from the menu.')
        elif choice == 'e':
            return
        else:
            print(f'\nIncorrect menu option selected: {choice}. Please select an option from the menu.')

if __name__ == '__main__':
    menu()
    




