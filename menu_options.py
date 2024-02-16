# from group_data import GroupData

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
            show_guest_menu()
            choice = input("\nSelect Option from Menu: ").lower()
            if choice == '1':
                print("\nMenu Option in Progress.")
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
    




