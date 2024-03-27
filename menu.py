menu_main_screen = """
        ________________________________________________________________

        Main Menu
        ________________________________________________________________

        1. List All Events
        2. Add New Event
        3. Edit Existing Event
        4. Generate Thank You Message For Event Guests
        5. Exit

        Select Option from Menu: """

menu_add_new_event_screen = """
        ________________________________________________________________

        Add New Event
        ________________________________________________________________

        1. Event Name
        2. Event Type
        3. Event Address
        4. Event Date
        5. Event Guests (Parties)
        6. Exit to Main Menu

        Select Option from Menu: """

menu_edit_event_screen = """
        ________________________________________________________________

        Edit Event
        ________________________________________________________________

        1. Change Event Name
        2. Change Event Date
        3. Change Event Type
        4. Change Event Address
        5. Edit Event Guests (Parties)
        6. Exit to Main Menu

        Select Option from Menu: """

menu_generate_message_screen = """
        ________________________________________________________________

        Thank You Message Generator
        ________________________________________________________________

        1. Generate Message for Individual Guest
        2. Generate Message for Guest Party
        3. Exit to Main Menu

        Select Option from Menu: """


def list_all_events():
    pass

# Add Event


def add_event_name():
    pass


def add_event_type():
    pass


def add_event_address():
    pass


def add_event_date():
    pass


def add_event_guests():
    pass

# Edit Event


def change_event_name():
    pass


def change_event_date():
    pass


def change_event_type():
    pass


def change_event_address():
    pass


def edit_event_guests():
    pass

# Generate Thank You Message


def individual_thank_you_message():
    pass


def group_thank_you_message():
    pass


def add_new_event():
    while True:
        choice = int(input(menu_add_new_event_screen))
        match choice:
            case 1:
                add_event_name()
            case 2:
                add_event_type()
            case 3:
                add_event_address()
            case 4:
                add_event_date()
            case 5:
                add_event_guests()
            case 6:
                return
            case _:
                print(
                    "\n\nThe selected option is invalid. Please input a valid choice from the menu above.")
                return


def edit_existing_event():
    while True:
        choice = int(input(menu_edit_event_screen))
        match choice:
            case 1:
                change_event_name()
            case 2:
                change_event_date()
            case 3:
                change_event_type()
            case 4:
                change_event_address()
            case 5:
                edit_event_guests
            case 6:
                return
            case _:
                print(
                    "\n\nThe selected option is invalid. Please input a valid choice from the menu above.")
                return


def generate_thank_you_message():
    while True:
        choice = int(input(menu_generate_message_screen))
        match choice:
            case 1:
                individual_thank_you_message()
            case 2:
                group_thank_you_message()
            case 3:
                return
            case _:
                print(
                    "\n\nThe selected option is invalid. Please input a valid choice from the menu above.")
                return


def main_menu():
    """Main menu function"""
    while True:
        choice = int(input(menu_main_screen))
        match choice:
            case 1:
                list_all_events()
            case 2:
                add_new_event()
            case 3:
                edit_existing_event()
            case 4:
                generate_thank_you_message()
            case 5:
                return
            case _:
                print(
                    "\n\nThe selected option is invalid. Please input a valid choice from the menu above.")
                main_menu()


if __name__ == '__main__':
    main_menu()
