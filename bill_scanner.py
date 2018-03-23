import bill_grabber as bg

state = 'CO'
session_list = bg.get_session_list(state=state)
master_list = bg.get_master_list(state=state)
bill = bg.get_bill(bill_id='1053035')

specific_master_list = bg.get_master_list(state, '1477')

