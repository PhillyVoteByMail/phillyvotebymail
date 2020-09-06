import os

from pavotebymail.dataimport import load_config
from pavotebymail.dataimport.loader import DataLoader
from .tools import fixture_path


def test_philly_parse():
    philly_test_path = fixture_path('philly_schema_test.txt')
    field_parser, schema = load_config('philadelphia')
    
    items = list(DataLoader.load(schema, philly_test_path, field_parser))

    assert items[0]['first_name'] == 'BILL'
    assert items[0]['middle_name'] == None
    assert items[0]['last_name'] == 'APPLE'
    assert items[0]['suffix'] == None
    assert items[0]['id_number'] == '111111111-51'
    assert items[0]['party_code'] == 'D'
    assert items[0]['home_phone'] == '5555555555'
    assert items[0]['house_number'] == '1122'
    assert items[0]['house_number_suffix'] == None
    assert items[0]['street_name'] == 'PAVOTE ST'
    assert items[0]['apartment_number'] == None
    assert items[0]['address_line_2'] == None
    assert items[0]['city'] == 'PHILADELPHIA'
    assert items[0]['state'] == 'PA'
    assert items[0]['zip'] == '19111'
    assert items[0]['mail_address_1'] == None
    assert items[0]['mail_address_2'] == None
    assert items[0]['mail_city'] == None
    assert items[0]['mail_state'] == None
    assert items[0]['mail_zip'] == None
    assert items[0]['last_vote_date'] == None
    assert items[0]['election_1_vote_method'] == None
    assert items[0]['election_1_party'] == None

    assert items[1]['first_name'] == 'STAPLER'
    assert items[1]['middle_name'] == 'B'
    assert items[1]['last_name'] == 'HORSE'
    assert items[1]['suffix'] == 'JR'
    assert items[1]['id_number'] == '111111111-52'
    assert items[1]['party_code'] == 'LN'
    assert items[1]['home_phone'] == '5555555555'
    assert items[1]['house_number'] == '1123'
    assert items[1]['house_number_suffix'] == None
    assert items[1]['street_name'] == 'PAVOTE AVE'
    assert items[1]['apartment_number'] == None
    assert items[1]['address_line_2'] == None
    assert items[1]['city'] == 'PHILADELPHIA'
    assert items[1]['state'] == 'PA'
    assert items[1]['zip'] == '19111'
    assert items[1]['mail_address_1'] == None
    assert items[1]['mail_address_2'] == None
    assert items[1]['mail_city'] == None
    assert items[1]['mail_state'] == None
    assert items[1]['mail_zip'] == None
    assert items[1]['last_vote_date'] == None
