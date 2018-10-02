Patient Endpoints
---------------------------------

.. code::

    This module contains all of Patient module endpoints.
    In order to be able to request endpoints, you need to use auth user
    The Test user and password are : Jason:secret

**The supports of Patient endpoints**

- Support to register a patient account
- Support to Sign in the MAPS with a patient account
- Support to update a patient information
- Support to get all patients
- Support to get obe patient by primary key
- Support to get calendar events by calendar id
- Support to update event by calendar id and event id
- Support to delete event by calendar id and event id
- Support to add appointments into db
- Support to get appointments by patient id
- Support to delete appointment by event id


**Endpoints**

**POST : http://Jason:secret@localhost:8081/api/v1.0/patient/register**

- Add a new patient account

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "patient": {
            "username": "test2",
            "email": "test2@test.com",
            "password": "123123",
            "created_at": "2018-09-09 21:00:00"
        }
    }

**Response Payload:**

.. code::

    {
        "code": 1,
        "msg": "Successfully Created!"
    }

    
---------------------

**POST : http://Jason:secret@localhost:8081/api/v1.0/patient/login**

- Sign in patient

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "patient": {
            "username": "patient_1",
            "password": "patientpass"
        }
    }

**Response Payload:**

.. code::

    {
        "code": 1,
        "msg": "Successfully Signed In!"
    }
    
---------------------

**PUT : http://Jason:secret@localhost:8081/api/v1.0/patient/calendars/rmit.edu.au_494ojtkhfk9cjulq9ate685ug0@group.calendar.google.com/events/t5kddj5191vhujqv84pngh7tqo**

- Update events

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "event": {
            "summary": "Booked",
            "email": "patient@test.com",
            "delete": false
        }
    }

**Response Payload:**

.. code::

    {
        "code": 1,
        "data": {
            "attendees": [
                {
                    "email": "doctor1@maps.com",
                    "responseStatus": "needsAction"
                },
                {
                    "email": "test123123123@test.com",
                    "responseStatus": "needsAction"
                }
            ],
            "created": "2018-09-27T20:49:18.000Z",
            "creator": {
                "email": "s3620273@student.rmit.edu.au"
            },
            "description": "This is Event description",
            "end": {
                "dateTime": "2018-09-22T02:00:00+10:00",
                "timeZone": "Australia/Melbourne"
            },
            "etag": "\"3076175509242000\"",
            "htmlLink": "https://www.google.com/calendar/event?eid=dDVrZGRqNTE5MXZodWpxdjg0cG5naDd0cW8gcm1pdC5lZHUuYXVfNDk0b2p0a2hmazljanVscTlhdGU2ODV1ZzBAZw",
            "iCalUID": "t5kddj5191vhujqv84pngh7tqo@google.com",
            "id": "t5kddj5191vhujqv84pngh7tqo",
            "kind": "calendar#event",
            "location": "MARS",
            "organizer": {
                "displayName": "Calendar for doctor1@maps.com",
                "email": "rmit.edu.au_494ojtkhfk9cjulq9ate685ug0@group.calendar.google.com",
                "self": true
            },
            "reminders": {
                "useDefault": true
            },
            "sequence": 0,
            "start": {
                "dateTime": "2018-09-21T02:00:00+10:00",
                "timeZone": "Australia/Melbourne"
            },
            "status": "confirmed",
            "summary": "Free",
            "updated": "2018-09-28T00:22:30.335Z"
        },
        "msg": "Successfully fetched!"
    }
    
---------------------

**GET : http://Jason:secret@localhost:8081/api/v1.0/patient/all**

- get all patients

**Headers:**

.. code::

    Content-Type : application/json

**Response Payload:**

.. code::

    {
        "code": 1,
        "data": [
            {
                "age": 30,
                "birthday": "2018-09-09",
                "calendar_id": null,
                "email": "patient_1@maps.com",
                "id": 1,
                "name": "Lee",
                "password": "23d5c51afade7a8701186250777f3c055c94984ce3d4aaed11438c0c",
                "phone": "402358178",
                "sex": 1,
                "username": "patient_1"
            }
        ],
        "msg": "Successfully Fetched!"
    }
    
---------------------


**GET : http://Jason:secret@localhost:8081/api/v1.0/patient/1**

- Get one patient

**Headers:**

.. code::

    Content-Type : application/json

**Response Payload:**

.. code::

    {
        "code": 1,
        "data": {
            "age": 30,
            "birthday": "2018-09-09",
            "calendar_id": null,
            "email": "patient_1@maps.com",
            "id": 1,
            "name": "Lee",
            "password": "23d5c51afade7a8701186250777f3c055c94984ce3d4aaed11438c0c",
            "phone": "402358178",
            "sex": 1,
            "username": "patient_1"
        },
        "msg": "Successfully Fetched!"
    }
    
---------------------


**POST : http://Jason:secret@localhost:8081/api/v1.0/patient/appointments**

- Create one appointment

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "appointment": {
            "patient_id": "1",
            "doctor_id": "1",
            "appointed_from": "2018-09-28T02:30:00+10:00",
            "appointed_to": "2018-09-28T05:30:00+10:00",
            "google_calendar_id": "",
            "google_event_id": "",
            "created_at": "2018-09-21 21:15:00"
        }
    }

**Response Payload:**

.. code::

    {
        "code": 1,
        "msg": "Successfully Created!"
    }
    
---------------------

**GET : http://Jason:secret@localhost:8081/api/v1.0/patient/1/appointments**

- Get all appointments

**Headers:**

.. code::

    Content-Type : application/json

**Response Payload:**

.. code::

    {
        "code": 1,
        "data": [
            {
                "appointed_from": "2018-10-01T00:30:00",
                "appointed_to": "2018-10-01T02:30:00",
                "created_at": "2018-09-30T00:04:28+00:00",
                "diagnoses": "Test2",
                "doctor": {
                    "age": 40,
                    "calendar_id": "rmit.edu.au_6ch9mp71j3crcb9kdd0tit4u88@group.calendar.google.com",
                    "created_at": "2018-09-29T23:58:43+00:00",
                    "email": "doctor1@maps.com",
                    "id": 1,
                    "name": "Lee",
                    "password": "23d5c51afade7a8701186250777f3c055c94984ce3d4aaed11438c0c",
                    "phone": "402358178",
                    "sex": 2,
                    "username": "doctor_1"
                },
                "doctor_id": 1,
                "google_calendar_id": "rmit.edu.au_6ch9mp71j3crcb9kdd0tit4u88@group.calendar.google.com",
                "google_event_id": "phnmmt9em0o2t78r9ig76hv44c",
                "id": 2,
                "notes": "Test1",
                "patient_id": 1
            },
            {
                "appointed_from": "2018-10-02T09:15:00",
                "appointed_to": "2018-10-02T09:30:00",
                "created_at": "2018-10-01T19:45:54+00:00",
                "diagnoses": "",
                "doctor": {
                    "age": 40,
                    "calendar_id": "rmit.edu.au_6ch9mp71j3crcb9kdd0tit4u88@group.calendar.google.com",
                    "created_at": "2018-09-29T23:58:43+00:00",
                    "email": "doctor1@maps.com",
                    "id": 1,
                    "name": "Lee",
                    "password": "23d5c51afade7a8701186250777f3c055c94984ce3d4aaed11438c0c",
                    "phone": "402358178",
                    "sex": 2,
                    "username": "doctor_1"
                },
                "doctor_id": 1,
                "google_calendar_id": "rmit.edu.au_6ch9mp71j3crcb9kdd0tit4u88@group.calendar.google.com",
                "google_event_id": "9qdrl84ee8ojj4bjl6o6dqrhf8",
                "id": 15,
                "notes": "",
                "patient_id": 1
            },
            {
                "appointed_from": "2018-09-28T02:30:00+10:00",
                "appointed_to": "2018-09-28T05:30:00+10:00",
                "created_at": "2018-09-21T21:15:00+00:00",
                "diagnoses": null,
                "doctor": {
                    "age": 40,
                    "calendar_id": "rmit.edu.au_6ch9mp71j3crcb9kdd0tit4u88@group.calendar.google.com",
                    "created_at": "2018-09-29T23:58:43+00:00",
                    "email": "doctor1@maps.com",
                    "id": 1,
                    "name": "Lee",
                    "password": "23d5c51afade7a8701186250777f3c055c94984ce3d4aaed11438c0c",
                    "phone": "402358178",
                    "sex": 2,
                    "username": "doctor_1"
                },
                "doctor_id": 1,
                "google_calendar_id": "",
                "google_event_id": "",
                "id": 16,
                "notes": null,
                "patient_id": 1
            }
        ],
        "msg": "Successfully Fetched!"
    }   
    
---------------------


**DELETE : http://Jason:secret@localhost:8081/api/v1.0/patient/appointments/0hst8b5v55ccjio242ln99tb38**

- Delete one appointment

**Headers:**

.. code::

    Content-Type : application/json

**Response Payload:**

.. code::

    {
        "code": 1,
        "msg": "Successfully Deleted!"
    }

---------------------

**PUT : http://Jason:secret@localhost:8081/api/v1.0/patient/testpatient**

- Update patient information

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "patient": {
            "name": "test",
            "age": 20
        }
    }

**Response Payload:**

.. code::

    {
        "code": 1,
        "msg": "Successfully Updated!"
    }

