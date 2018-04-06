#print out the lobbyists
# and the bills they are involved with
# and whether they are for or against or ..??

import csv
import re
from collections import namedtuple


filename = 'data/Bill_Information_and_Position_with_Income_of_Lobbyist_in_Colorado.csv'
column = 'billInformationAndPosition'
lobbyist_last_name = 'lobbyistLastName'
lobbyist_first_name = 'lobbyistFirstName'

HOUSE_BILL = 'HB[0-9]+'
SENATE_BILL = 'SB[0-9]+'

POSITION_LIST = ('supporting', 'monitoring', 'amending', 'opposing')

BillInfo = namedtuple('BillInfo', ['number', 'position'])


def find_all_bill_numbers(field):
    """

    Extract HB or SB list from field, with whether lobbyist's position is:
    - Supporting
    - Monitoring
    - Amending
    - Opposing
    - .. and also JBC (Joint Budget Committee [non-partisan research])

    Args:
        field:   field containing bill information

    Returns:
        list of House Bill numbers and/or Senate Bill Numbers from field

    """
    # remove whitespace so bill info is easier to parse
    field_no_white_space = field.replace(" ", "")
    hb_matches = re.findall(HOUSE_BILL, field_no_white_space)
    sb_matches = re.findall(SENATE_BILL, field_no_white_space)

    return hb_matches + sb_matches   # return list of bills from field


def bill_info(field):
    """

    Args:
        field:

    Returns:
        collection of tuples of bill number and position

    """
    # for every bill number in field
    #   extract the bill number
    #   extract the postion for that bill
    # return the list of bills and positions
    bill_list = []
    elements = field.split(',')
    for elem in elements:
        hb_match = re.search(HOUSE_BILL, elem.replace(" ", ""))
        sb_match = re.search(SENATE_BILL, elem.replace(" ", ""))
        if hb_match:
            position = find_position(elem.lower())
            if position:
                bill_list.append(BillInfo(elem[hb_match.start():hb_match.end()-1], position))
        elif sb_match:
            position = find_position(elem.lower())
            if position:
                bill_list.append(BillInfo(elem[sb_match.start():sb_match.end()-1], position))

    return bill_list


def find_position(text):
    """
    Determine position (Opposing, Supporting, etc..) from text

    JBC means Joint Budget Council and is neutral.

    Args:
        text:

    Returns:
        pos if found.

    """
    for pos in POSITION_LIST:
        if text.count(pos):
            return pos



def process_line(line):
    """
    Process the line and return list of records

    Args:
        line:

    Returns:
        list of records:  lobbyist id, bill no., bill position

    """
    records = []
    for billinfo in bill_info(line['billInformationAndPosition']):
        records.append({'primaryLobbyistID': line['primaryLobbyistID'], 'Bill#': billinfo.number, 'position': billinfo.position})
    return records


def main():
    """
    reads bill info from csv

    writes out a record:
    primaryLobbyistID, Bill No, position (support/oppose/etc..)

    """
    reader = csv.DictReader(open(filename, 'r'))
    output_header = ['primaryLobbyistID', 'Bill#', 'position']
    writer = csv.DictWriter(open('output.csv', 'w'), output_header)
    writer.writeheader()

    for line in reader:
        for record in process_line(line):
            writer.writerow(record)
        # print(", ".join(record[lobbyist_last_name], record[lobbyist_first_name]) + " " + bill_info(record))



if __name__ == '__main__':
    main()