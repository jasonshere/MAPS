# import necessary packages
from init import PROTOCOL, APIKEY, APIPASS, SERVICE_ADDRESS
import requests
import json
import time

class PatientService():
    # constructor
    def __init__(self):
        self.module = 'patient'
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

    # request API of login
    def update(self, payload):
        try:
            url = self.baseUrl + '/' + payload['patient']['username']
            headers = {'Content-type': 'application/json'}
            response = requests.put(url, data=json.dumps(payload), headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # request API of login
    def createCalendar(self, payload):
        try:
            url = self.baseUrl + '/calendars'
            headers = {'Content-type': 'application/json'}
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # request API of login
    def createEvent(self, payload, calendarId):
        try:
            url = self.baseUrl + '/calendars/' + calendarId + '/events'
            headers = {'Content-type': 'application/json'}
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # get patient by id
    def getPatientById(self, patient_id):
        try:
            url = self.baseUrl + '/{}' .format(patient_id)
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # get events
    def getAllEvents(self, calendarId):
        try:
            url = self.baseUrl + '/calendars/' + calendarId + '/events'
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # delete event
    def deleteEventById(self, calendarId, eventId):
        try:
            url = self.baseUrl + '/calendars/' + calendarId + '/events/' + eventId
            headers = {'Content-type': 'application/json'}
            response = requests.delete(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # create event connector
    def createEventConnector(self, payload):
        try:
            url = self.baseUrl + '/appointments'
            headers = {'Content-type': 'application/json'}
            pl = {
                "appointment": {
                    "patient_id": payload['patient_id'],
                    "doctor_id": payload['doctor_id'],
                    "appointed_from": payload['start'],
                    "appointed_to": payload['end'],
                    "google_event_id": payload['google_event_id'],
                    "google_calendar_id": payload['google_calendar_id'],
                    "created_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                }
            }
            print(pl)
            response = requests.post(url, data=json.dumps(pl), headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # get event connector
    def getEventConnector(self, doctorId):
        try:
            url = self.baseUrl + '/appointments/' + doctorId
            headers = {'Content-type': 'application/json'}
            
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)


    