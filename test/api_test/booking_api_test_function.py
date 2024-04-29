import requests
import json
from jsonpath_ng import jsonpath
from jsonschema import validate
from requests.auth import HTTPBasicAuth


base_url = "https://restful-booker.herokuapp.com/booking/"
booking_id = ''

def test_create_new_booking_id():
    payload = {
            "firstname": "Crab",
            "lastname": "Brown",
            "totalprice": 133,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-04-12",
                "checkout": "2024-04-29"
            },
            "additionalneeds": "Cacao"
    }
    response = requests.post(url=base_url, json=payload)
    assert response.status_code == 200
    # checking json schema
    schema = {
    "type" : "object",
    "properties" : {
        "bookingid" : {"type" : "number"},
        "booking" : {"type" : "object"},
    },
    "required": ["bookingid", "booking"],
    }
    validate(instance=response.json(), schema=schema)
    # checking response body is matched with payload
    response_content = response.json()
    global booking_id
    booking_id = response_content["bookingid"]
    booking_detail = response_content["booking"]
    assert booking_detail == payload
    


def test_get_a_booking_id():
    response = requests.get(url=base_url + str(booking_id))
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body) > 0
    schema = {
        "type" : "object",
        "items" : {
            "additionalProperties" : False,
            "properties" : {
                "firstname" : {"type" : "string"},
                "lastname" : {"type" : "string"},
                "totalprice" : {"type" : "number"},
                "depositpaid" : {"type" : "boolean"},
                "bookingdates" : {
                    "type" : "object",
                    "properties": {
                        "checkin" : {"type" : "string", "format":"date-time"},
                        "checkout" : {"type" : "string", "format":"date-time"}
                    }
                    },
            },
            "required" : ["firstname","lastname","totalprice","bookingdates"]
        
        },
    }
    validate(instance = response.json(), schema= schema)



def test_update_a_booking():
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }   
    basic = HTTPBasicAuth(username='admin', password='password123')
    update_payload = {
        "firstname" : "Pepsico",
        "lastname" : "Brownie",
        "totalprice" : 1283,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2023-12-01",
            "checkout" : "2023-12-20"
        },
        "additionalneeds" : "Lunch"
    }
    payload_json = json.dumps(update_payload)
    response = requests.put(url = base_url + str(booking_id), auth=basic, 
                            headers=headers, data= payload_json)
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body) > 0
    schema = {
        "type" : "object",
        "items" : {
            "additionalProperties" : False,
            "properties" : {
                "firstname" : {"type" : "string"},
                "lastname" : {"type" : "string"},
                "totalprice" : {"type" : "number"},
                "depositpaid" : {"type" : "boolean"},
                "bookingdates" : {
                    "type" : "object",
                    "properties": {
                        "checkin" : {"type" : "string", "format":"date-time"},
                        "checkout" : {"type" : "string", "format":"date-time"}
                    }
                    },
            },
            "required" : ["firstname","lastname","totalprice","bookingdates"]
        
        },
    }
    validate(instance = response.json(), schema = schema)
    booking_info = response.json()
    assert booking_info == update_payload
    print(response_body)

def test_partial_update_a_booking():
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }   
    basic = HTTPBasicAuth(username='admin', password='password123')
    update_payload = {
        "bookingdates" : {
            "checkin" : "2023-12-01",
            "checkout" : "2023-12-18"
        },
        "additionalneeds" : "Dinner"
    }
    payload_json = json.dumps(update_payload)
    response = requests.patch(url = base_url + str(booking_id), auth=basic, 
                            headers=headers, data= payload_json)
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body) > 0
    schema = {
        "type" : "object",
        "items" : {
            "additionalProperties" : False,
            "properties" : {
                "firstname" : {"type" : "string"},
                "lastname" : {"type" : "string"},
                "totalprice" : {"type" : "number"},
                "depositpaid" : {"type" : "boolean"},
                "bookingdates" : {
                    "type" : "object",
                    "properties": {
                        "checkin" : {"type" : "string", "format":"date-time"},
                        "checkout" : {"type" : "string", "format":"date-time"}
                    }
                    },
            },
            "required" : ["firstname","lastname","totalprice","bookingdates"]
        
        },
    }
    validate(instance = response.json(), schema = schema)
    assert response.json()["bookingdates"] == update_payload["bookingdates"]
    assert response.json()["additionalneeds"] == update_payload["additionalneeds"]
    print(response_body)
