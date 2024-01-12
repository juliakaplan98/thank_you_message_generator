import pandas as pd

def get_guest_data():
    # empty list of guest data 
    guest_list = []
    # read csv file containing guest contact information
    guest_df = pd.read_csv('C:/Users/julia/OneDrive/Desktop/My Guest List.csv')

    # iterate over each guest
    for ind in guest_df.index:
        # use dict to store individual guest information
        guest_data = dict({'Party': guest_df['Party'][ind], 'Full Name': f"{guest_df['First Name'][ind]} {guest_df['Last Name'][ind]}", 'Attendance Status': guest_df['Wedding Ceremony & Reception - RSVP'][ind]})
        # store all guest information in list
        guest_list.append(guest_data)
    return (guest_list)


def get_party_data(guest_list):
        party_list = []
        # iterate over each guest and append each unique party to list
        for guest in guest_list:
            for key, val in guest.items():
                if key == 'Party':
                     if val not in party_list:
                        party_list.append(val)         
        return party_list



guest_list = get_guest_data()
party_list = get_party_data(guest_list)

print(len(party_list))