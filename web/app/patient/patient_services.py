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

    # get events by doctor id
    def getEventsByDoctorId(self, doctorId):
        try:
            baseUrl = '{}://{}:{}@{}/{}'. format(PROTOCOL, APIKEY, APIPASS, SERVICE_ADDRESS, 'doctor')
            url = baseUrl + '/' + doctorId
            headers = {'Content-type': 'application/json'}
            
            response = requests.get(url, headers=headers)
            
            if response.json()['code'] == 1:
                # get calendar_id
                calendarId = response.json()['data']['calendar_id']
                if len(calendarId) is 0:
                    raise Exception('no calendar')
                else:
                    url = baseUrl + '/calendars/{}/events' .format(calendarId)
                    headers = {'Content-type': 'application/json'}
                    ret = requests.get(url, headers=headers)
                    
                    return True, ret.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, {'data': str(e)}

    # get events by doctor id
    def updateEventsByDoctorId(self, doctorId, eventId, email, delete):
        try:
            baseUrl = '{}://{}:{}@{}/{}'. format(PROTOCOL, APIKEY, APIPASS, SERVICE_ADDRESS, 'doctor')
            url = baseUrl + '/' + doctorId
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                # get calendar_id
                calendarId = response.json()['data']['calendar_id']
                if len(calendarId) is 0:
                    raise Exception('no calendar')
                else:
                    url = self.baseUrl + '/calendars/{}/events/{}' .format(calendarId, eventId)
                    headers = {'Content-type': 'application/json'}
                    print(delete)
                    if delete == "false":
                        payload = {
                            'event': {
                                'summary': 'Booked',
                                'email': email,
                                'delete': "false"
                            }
                        }
                    else:
                        payload = {
                            'event': {
                                'summary': 'Free',
                                'email': email,
                                'delete': "true"
                            }
                        }
                    print(payload)
                    ret = requests.put(url, data=json.dumps(payload), headers=headers)
                    return True, ret.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, {'data': str(e)}

    # set appointment
    def setAppointment(self, eventId, doctorId, patientId, start, end):
        try:
            baseUrl = '{}://{}:{}@{}/{}'. format(PROTOCOL, APIKEY, APIPASS, SERVICE_ADDRESS, 'doctor')
            url = baseUrl + '/' + doctorId
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                # get calendar_id
                calendarId = response.json()['data']['calendar_id']
                if len(calendarId) is 0:
                    raise Exception('no calendar')
                else:
                    url = self.baseUrl + '/appointments'
                    headers = {'Content-type': 'application/json'}
                    payload = {
                        "appointment": {
                            "patient_id": patientId,
                            "doctor_id": doctorId,
                            "appointed_from": start,
                            "appointed_to": end,
                            "google_calendar_id": calendarId,
                            "google_event_id": eventId,
                            "created_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        }
                    }
                    response = requests.post(url, data=json.dumps(payload), headers=headers)
                    if response.json()['code'] == 1:
                        return True, response.json()
                    else:
                        return False, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # set appointment
    def deleteAppointment(self, eventId):
        try:
            url = self.baseUrl + '/appointments/{}'. format(eventId)
            headers = {'Content-type': 'application/json'}
            response = requests.delete(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
            
        except Exception as e:
            return False, str(e)

    # get all appointments
    def getAppointmentsById(self, patientId):
        try:
            url = self.baseUrl + '/{}/appointments'. format(patientId)
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
            
        except Exception as e:
            return False, str(e)