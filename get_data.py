from guest_data.party import Party



def show_menu():
    print("Wedding Thank You Message Generator Menu")
    print("----------------------------------------")
    print("(1) Add New Guest")
    print("(2) Add Information to Existing Guest")
    print("(3) Show Existing Guests")
    print("(E) Exist")

def new_guest_entry():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    attendance_status = input("Attendance Status (Y/N): ")
    gift_status = input("Gift Received (Y/N): ")
    if gift_status == 'Y':
        gift_item = input("Gift Item: ")

def menu():
    while True:
        show_menu()
        choice = input("Select Option from Menu: ").lower()
        if choice == '1':
            new_guest_entry()
        elif choice == '2':
            print("Menu Selection in Progress")
        elif choice == '3':
            print("Menu Selection in Progress")
        elif choice == 'e':
            return
        else:
            print(f'Incorrect menu option selected: {choice}. Please select an option from the menu.')

if __name__ == '__main__':
    menu()
    




