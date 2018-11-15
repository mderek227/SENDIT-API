"""CONFIG FOR TESTING ENDPOINTS"""
import pytest
from app import create_app

EMPTY_ORDER = {}

DELIVERY = {"pick_up":"Ntinda",            
            "destination":"Nakawa",
            "parcel_name":"Radio",
            "price":"10000",            
            "user_id": "derek"
            }

MISSING_KEYS = {
                "destination":"Bukoto",
                "parcel_name":"Television",
                "price":"15000",                
                "user_id": "derek"
                }

EMPTY_FIELDS = {"pick_up":"",                
                "destination":"Bukoto",
                "parcel_name":"Television",
                "description":"15000",                
                "user_id": "derek"
               }

@pytest.fixture(scope='module')
def set_up_client():
    """create new app that will be used for a test"""
    #creating new flask app and a test client
    app = create_app('test')
    client = app.test_client()

    #creating the application context and
    #allowing test functions to run by calling test client
    #and finally cleaning house
    ctx = app.app_context()
    ctx.push()
    yield client
    ctx.pop()
