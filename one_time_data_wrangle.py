import pandas as pd
import os
from sqlalchemy import create_engine
import zipfile


def main():

    directory_name = "data"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        zip_ref = zipfile.ZipFile('./data.zip', 'r')
        zip_ref.extractall('./')
        zip_ref.close()

    db = create_engine('postgresql://@localhost:5432/leglobber')

    file_list = [{"table": 'bill_info', 'filename': "data/Bill_Information_and_Position_with_Income_of_Lobbyist_in_Colorado.csv"},
                 {"table": 'client_characterization', 'filename': "data/Characterization_of_Lobbyist_Clients_in_Colorado.csv"},
                 {"table": 'client_directory', 'filename': "data/Directory_of_Lobbyist_Clients_in_Colorado.csv"},
                 {"table": 'lobbyist_directory', 'filename': "data/Directory_of_Lobbyists_in_Colorado.csv"},
                 {"table": 'lobbyist_expenses', 'filename': "data/Expenses_for_Lobbyists_in_Colorado.csv"},
                 {"table": 'lobbyist_subcontractors', 'filename': "data/Subcontractors_for_Lobbyists_in_Colorado.csv"}]

    for file in file_list:
        data = pd.read_csv(file['filename'])
        data.to_sql(name=file['table'], con=db, if_exists='replace')

    db.dispose()

if __name__ == '__main__':
    main()
