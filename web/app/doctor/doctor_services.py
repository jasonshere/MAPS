# import necessary packages
from init import PROTOCOL, APIKEY, APIPASS, SERVICE_ADDRESS
import requests
import json
import time

class DoctorService():
    # constructor
    def __init__(self):
        self.module = 'doctor'
        self.baseUrl = '{}://{}:{}@{}/{}'. format(PROTOCOL, APIKEY, APIPASS, SERVICE_ADDRESS, self.module)

    # request API of registering patients
    def register(self, payload):
        try:
            url = self.baseUrl + '/register'
            headers = {'Content-type': 'application/json'}
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

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

    # request API of get all doctors
    def getAll(self):
        try:
            url = self.baseUrl + '/all'
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # request API to set datetime that is not available
    def setBusyTime(self, payload):
        try:
            url = self.baseUrl + '/busytimes'
            headers = {'Content-type': 'application/json'}
            payload = {
                'busytime': {
                    "doctor_id": payload['doctor_id'],
		            "busytime_from": payload['start'],
		            "busytime_to": payload['end'],
		            "created_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                }
            }
            print(payload)
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)
    
    # get all busytime
    def getBusyTimes(self, doctor_id):
        try:
            url = self.baseUrl + '/{}/busytimes'. format(doctor_id)
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # delete busytime
    def deleteBusyTimes(self, busyid):
        try:
            url = self.baseUrl + '/busytimes/{}'. format(busyid)
            headers = {'Content-type': 'application/json'}
            response = requests.delete(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)