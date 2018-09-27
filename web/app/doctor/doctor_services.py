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

    # request API to set datetime that is available
    def setFreeTime(self, inputPayload):
        try:
            url = self.baseUrl + '/calendars'
            headers = {'Content-type': 'application/json'}
            payload = {
                'calendar': {
                    "summary": "Calendar for {}". format(inputPayload['doctor_email']),
                    "description": "Doctor's calendar",
                    "location": "MAPS",
                    "timezone": "Australia/Melbourne",
                    "customer_id": inputPayload['doctor_id']
                }
            }
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            
            if response.json()['code'] == 1:
                # request create event
                eventPayload = {
                    "event": {
                        "summary": "Free",
                        "description": "Free Time",
                        "location": "MAPS",
                        "timezone": "Australia/Melbourne",
                        "start": inputPayload['start'],
                        "end": inputPayload['end'],
                        "patient_email": "info@maps.com",
                        "doctor_email": inputPayload['doctor_email']
                    }
                }
                calendarId = response.json()['data']['calendar_id']
                eventUrl = self.baseUrl + '/calendars/{}/events'. format(calendarId)
                ret = requests.post(eventUrl, data=json.dumps(eventPayload), headers=headers)
                return True, ret.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # request API to get all events
    def getFreeTime(self, calendarId):
        try:
            url = self.baseUrl + '/calendars/{}/events'. format(calendarId)
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # delete freetime
    def deleteFreeTime(self, calendarId, freeId):
        try:
            url = self.baseUrl + '/calendars/{}/events/{}'. format(calendarId, freeId)
            headers = {'Content-type': 'application/json'}
            response = requests.delete(url, headers=headers)
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
    def deleteBusyTime(self, busyid):
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

    # get doctor by id
    def getDoctorById(self, doctor_id):
        try:
            url = self.baseUrl + '/' + doctor_id
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)
