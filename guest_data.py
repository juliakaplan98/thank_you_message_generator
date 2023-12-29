import pandas as pd


# read csv file containing guest contact information
guest_df = pd.read_csv('C:/Users/julia/OneDrive/Desktop/My Guest List.csv')
# print(guest_df)

# create df with guest full name, party, and attendance status
attendance_df = guest_df[['First Name','Last Name', 'Party', 'Wedding Ceremony & Reception - RSVP']].copy()
print(attendance_df)

