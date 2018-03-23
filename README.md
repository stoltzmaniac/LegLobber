# LegLobber
Legislation checker

Create virtual environment

`pip install -r requirements.txt`



----
The following is unnecessary for now:

This builds a database from the data.zip file

terminal: `psql`
within psql shell: `CREATE DATABASE leglobber;`  

terminal (within virtual environment): `python one_time_data_wrangle.py`

`python one_time_data_wrangle.py` (will unzip and create new folder if it does not exist) 