# import necessary packages
from init import PROTOCOL, APIKEY, APIPASS, SERVICE_ADDRESS
import requests
import json
import time

class DoctorService():
    # constructor
    def __init__(self):
        """
        constructor
        """
        self.module = 'doctor'
        self.baseUrl = '{}://{}:{}@{}/{}'. format(PROTOCOL, APIKEY, APIPASS, SERVICE_ADDRESS, self.module)

    # request API of registering patients
    def register(self, payload):
        """
        add a new doctor
        :param payload: payload
        :return: boolean,object
        """
        try:
            url = self.baseUrl + '/register'
            headers = {'Content-type': 'application/json'}
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            if response.json()['code'] == 1:
                url = self.baseUrl + '/calendars'
                headers = {'Content-type': 'application/json'}
                res, resData = self.getDoctorByEmail(payload['doctor']['email'])
                pl = {
                    'calendar': {
                        "summary": "Calendar for {}". format(payload['doctor']['email']),
                        "description": "Doctor's calendar",
                        "location": "MAPS",
                        "timezone": "Australia/Melbourne",
                        "customer_id": resData['data']['id']
                    }
                }
                response = requests.post(url, data=json.dumps(pl), headers=headers)
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # request API of login
    def login(self, payload):
        """
        sign in as a doctor
        :param payload: payload
        :return: boolean,object
        """
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
        """
        get all doctors
        :return: boolean,object
        """
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
        """
        set free time
        :param inputPayload: payload
        :return:boolean,object
        """
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
        """
        get free time
        :param calendarId: calendar id
        :return: boolean,object
        """
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
        """
        delete free time
        :param calendarId: calendar id
        :param freeId: app id
        :return: boolean,object
        """
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

    # get doctor by id
    def getDoctorById(self, doctor_id):
        """
        get doctor by id
        :param doctor_id: doctor id
        :return: boolean,object
        """
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

    # get doctor by email
    def getDoctorByEmail(self, doctor_email):
        """
        get a doctor by email
        :param doctor_email: doctor email
        :return: boolean,object
        """
        try:
            url = self.baseUrl + '/email/' + doctor_email
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # get patients
    def getAllPatients(self, doctor_id):
        """
        get all patients
        :param doctor_id: doctor id
        :return: boolean,object
        """
        try:
            url = self.baseUrl + '/{}/appointments'. format(doctor_id)
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)

    # edit notes
    def editNotes(self, appointmentId, notes):
        """
        add notes by appiintment id
        :param appointmentId: appointment id
        :param notes: notes
        :return: boolean,object
        """
        try:
            url = self.baseUrl + '/appointments/{}'. format(appointmentId)        
            headers = {'Content-type': 'application/json'}
            payload = {
                "appointment": {
                    "notes": notes
                }
            }
            response = requests.put(url, data=json.dumps(payload), headers=headers)
            if response.json()['code'] == 1:
                return True
            return False
        except Exception as e:
            return False, str(e)

    # edit diagnoses
    def editDiags(self, appointmentId, diags):
        """
        edit diagnoses by appointment id
        :param appointmentId: appointment id
        :param diags: diagnoses
        :return: boolean,object
        """
        try:
            url = self.baseUrl + '/appointments/{}'. format(appointmentId)        
            headers = {'Content-type': 'application/json'}
            payload = {
                "appointment": {
                    "diagnoses": diags
                }
            }
            response = requests.put(url, data=json.dumps(payload), headers=headers)
            if response.json()['code'] == 1:
                return True
            return False
        except Exception as e:
            return False, str(e)

    # get appointment by id
    def getAppointmentById(self, appointment_id):
        """
        get appointment by app id
        :param appointment_id: app id
        :return: boolean,object
        """
        try:
            url = self.baseUrl + '/appointments/{}'. format(appointment_id)
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e) 

    # get all appointments by patient id
    def getAppointmentsByPatientId(self, patient_id):
        """
        get appointment by patient id
        :param patient_id: patient id
        :return: boolean,object
        """
        try:
            url = self.baseUrl + '/appointments/patient/{}'. format(patient_id)
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)
    
    def getNextPatientByDoctorId(self, doctor_id):
        """
        get next patient by doctor id
        :param doctor_id: doctor id
        :return: boolean,object
        """
        try:
            url = self.baseUrl + '/{}/appointments/next_patient'. format(doctor_id)
            headers = {'Content-type': 'application/json'}
            response = requests.get(url, headers=headers)
            if response.json()['code'] == 1:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as e:
            return False, str(e)



