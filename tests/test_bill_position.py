import pytest
from bill_position import bill_info, find_all_bill_numbers


@pytest.mark.parametrize('field, expected', [
    ('HB1000', ['HB1000']),
    ('HB111  HB22222', ['HB111', 'HB22222'])])
def test_find_all_bill_numbers(field, expected):
    result = find_all_bill_numbers(field)
    assert result == expected


def test_bill_info():
    field =('HB 1081 Supporting BILL TO REQUIRING LIICENSING OF POWERSPORTS DEALERS BY MOTOR VEHICLE DEALER BOARD, ' 
           'HB 1081 Supporting GIVES THE MOTOR VEHICLE DEALER BOARD AUTHORITY OVER SALES OF POWERSPORTS PRODUCTS, '
            'HB 1081 Supporting HB1081 ON BEHALF OF THE POWERSPORTS DEALERS ASSOCIATION OF COLORADO ADDS A LICNSE REQUIREMENT TO SELL POWERSPORTS PRODUCTS, '
            'HB 1081 Supporting LICENSE POWERSPORTS DEALERS, '
            'HB 1081 Supporting REQUIRES LICENSING OF POWERSPORTS  DEALERAS AND MANUFACTURERS, '
            'HB 1081 Supporting REQUIRES LICENSING OF POWERSPORTS  DEALERS AND MANUFACTURERS, '
            'HB 1081 Supporting SUPPORT AND LOBBY BILL THROUGH THE HOUSE.  LICENSING OF POWERSPORTS DEALERS, '
            'SB 112 Opposing ALLOWS LENDERS TO SELL REPOSSED MOTOR VEHICLES WITHOUT A MOTOR VEHICLE DEALER LICENSE.  OPPOSE AS WRITTEN, '
            'SB 221 Supporting MOTOR VEHICLE DEALER BOARD SUNRISE, '
            'SB 221 Supporting SUPPORT, '
            'WORKING ON THE REAUTHORIZATION OF THE MOTOR VEHICLE DEALER LICENSING BOARD')
    result = bill_info(field)
    assert len(result) == 10
