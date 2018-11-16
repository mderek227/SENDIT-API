"""TEST ENDPOINTS"""
import json
from .conftest import  EMPTY_FIELDS, EMPTY_ORDER, MISSING_KEYS, DELIVERY

def test_delivery_order_with_no_data(set_up_client):
    """Test whether the user has submitted an empty post"""
    response = set_up_client.post('api/v1/parcels', data=json.dumps(EMPTY_ORDER), content_type='application/json')
    assert response.status_code == 400
    assert 'You entered nothing' in response.data

def test_delivery_oder_with_missing_values(set_up_client):
    """test whether the user has submitted a post with missing values"""
    response = set_up_client.post('api/v1/parcels',  data=json.dumps(EMPTY_FIELDS), content_type='application/json')
    assert response.status_code == 400
    assert 'You are missing pick_up in your input' in response.data

def test_delivery_order_with_missing_keys(set_up_client):
    """test whether the user is missing some fields"""
    response = set_up_client.post('api/v1/parcels',  data=json.dumps(MISSING_KEYS), content_type='application/json')
    assert response.status_code == 400
    assert 'You are missing a required field' in str(response.json)

def test_make_order(set_up_client):
    """Test to create a delivery order """
    response = set_up_client.post('api/v1/parcels', data=json.dumps(DELIVERY), content_type='application/json')
    assert response.status_code == 201
    assert 'Delivery order created'in str(response.json)

def test_see_all_order(set_up_client):
    """test to see all orders"""
    response = set_up_client.get('api/v1/parcels', content_type='application/json')
    assert response.status_code == 200
    assert 'You dont have any delivery orders' in str(response.json)

def test_get_all_orders_by_userid(set_up_client):
    """test to see all orders when none exist"""
    reponse = set_up_client.get('api/v1/users/derek/parcels')
    assert reponse.status_code == 200
    assert 'You have not made any delivery orders' in  str(reponss.json)


def test_cancel_delivery_order(set_up_client):
    """cancel a delivery order"""
    response = set_up_client.put('api/v1/parcels/3/cancel')
    assert response.status_code == 200
    assert 'Delivery order 3 not found' in str(response.json)

def test_cancel_delivery_order_with_id(set_up_client):
    """cancel a delivery order"""
    #testing with a delivery order in place
    response = set_up_client.post('api/v1/parcels',  data=json.dumps(DELIVERY), content_type='application/json')
    assert response.status_code == 201
    resp = set_up_client.put('api/v1/parcels/1/cancel')
    assert resp.status_code == 200
    assert 'delivery order has been canceled' in str(resp.json)