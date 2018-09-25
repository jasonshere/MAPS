# import necessary packages
from init import PROTOCOL, APIKEY, APIPASS, SERVICE_ADDRESS
import requests
import json

class ClerkService():
    # constructor
    def __init__(self):
        self.module = 'clerk'
        self.baseUrl = '{}://{}:{}@{}/{}'. format(PROTOCOL, APIKEY, APIPASS, SERVICE_ADDRESS, self.module)

    # request API of login
    def login(self, payload):
        try:
            url = self.baseUrl + '/login'
            headers = {'Content-type': 'application/json'}
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    