import bill_grabber as bg
import pandas as pd
import re


# Example of how to pull bills
# state = 'CO'
# session_list = bg.get_session_list(state=state)
# master_list = bg.get_master_list(state=state)
# bill = bg.get_bill(bill_id='1053035')
# specific_master_list = bg.get_master_list(state, '1477')

# Grab most recent master list, select most recently altered bill
state = 'CO'
master_list = bg.get_master_list(state=state).sort_values('last_action_date', ascending=False)
latest_bill = master_list.iloc[0]

lobby = pd.read_csv('data/Bill_Information_and_Position_with_Income_of_Lobbyist_in_Colorado.csv')
lobby[['incomeAmount']] = lobby[['incomeAmount']].replace('[\$,]', '', regex=True).astype(float)

# Regex to get bill number out of text and create new column in lobby
search = []
for values in lobby['billInformationAndPosition']:
    try:
        obj = re.search(r'(HB ([^\s]+))', values)
        text = obj.group()
    except:
        text = "NA"
    if text == "NA":
        try:
            obj = re.search(r'(SB ([^\s]+))', values)
            text = obj.group()
        except:
            text = "NA"
    search.append(text.replace(" ", ""))
lobby['billNumber'] = search


# Join lobby and master_list to get proper data
df = pd.merge(lobby, master_list, how='inner', left_on='billNumber', right_on='number')


lobby['fullName_pid'] = lobby['lobbyistLastName'] + "_" + lobby['lobbyistFirstName'] + "_" + lobby['primaryLobbyistID'].map(str)
lobby['fullName_aid'] = lobby['lobbyistLastName'] + "_" + lobby['lobbyistFirstName'] + "_" + lobby['annualLobbyistRegistrationID'].map(str)

top_paid_pid = lobby.groupby(['fullName_pid'])[['incomeAmount']].sum().sort_values('incomeAmount', ascending=False)
top_paid_aid = lobby.groupby(['fullName_aid'])[['incomeAmount']].sum().sort_values('incomeAmount', ascending=False)
