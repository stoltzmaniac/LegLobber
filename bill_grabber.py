import json
from urllib.parse import urlencode
from urllib.request import urlopen


# using the legiscan api: https://legiscan.com/legiscan (free tier)
api_creds = json.load(open('api_credentials.json'))
legiscan_token = api_creds['LEGISCAN_TOKEN']
base_url = "https://api.legiscan.com/?"

def get_bills_data(list_of_tuples):
    parameter_dict = {"key": legiscan_token}

    # list_of_tuples represents key value pair in request
    # example: https://api.com/?happy=new_year&merry=christmas
    # would need: [('happy', 'new_year'), ('merry', 'christmas')]
    for parameter in list_of_tuples:
        parameter_dict[parameter[0]] = parameter[1]
    parameters = urlencode(parameter_dict)
    request =  "{}{}".format(base_url, parameters)
    response = urlopen(request)
    raw_data = response.read()
    data = json.loads(raw_data.decode('utf-8'))
    return data


def get_session_list(state):
    bills = get_bills_data([('op', 'getSessionList'), ('state', state)])
    if bills['status'] == 'OK':
        return bills['sessions']
    else:
        return "Error with API call"


def get_master_list(state, session_id=None):
    # default session_id gives most recent year
    parameter_list = [('op','getMasterList'), ('state', state)]
    if session_id:
        parameter_list.append(('id', session_id))
    bills = get_bills_data(parameter_list)
    if bills['status'] == 'OK':
        return bills['masterlist']
    else:
        return "Error with API call"


def get_bill(bill_id):
    parameter_list = [('op', 'getBill'), ('id', bill_id)]
    bills = get_bills_data(parameter_list)
    if bills['status'] == 'OK':
        return bills
    else:
        return "Error with API call"
