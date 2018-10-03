Doctor Endpoints
---------------------------------

.. code::

    This module contains all of Doctor module endpoints.
    In order to be able to request endpoints, you need to use auth user
    The Test user and password are : Jason:secret

**The supports of Doctor endpoints**

- Support to register a doctor account
- Support to Sign in the MAPS with a doctor account
- Support to get all doctors
- Support to get one doctor by primary key
- Support to add calendar for doctor
- Support to add event for doctor
- Support to get events from google calendar
- Support to delete event by calendar id and event id
- Support to get one doctor by email
- Support to get appointments by doctor id
- Support to get doctor id by event id
- Support to update appointments by appointment id
- Support to get appointment by appointment id
- Support to get appointments by patient id


**Endpoints**

**POST : http://Jason:secret@localhost:8081/api/v1.0/doctor/register**

- Add a new doctor account

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "doctor": {
            "username": "test3",
            "email": "test3@test2.com",
            "password": "123123",
            "name": "doctor3",
            "phone": "123123123",
            "age": 20,
            "sex": 1,
            "created_at": "2018-09-09 21:00:00",
            "updated_at": "2018-09-09 21:00:00"
        }
    }

**Response Payload:**

.. code::

    {
        "code": 1,
        "msg": "Successfully Created!"
    }

    
---------------------

**POST : http://Jason:secret@localhost:8081/api/v1.0/doctor/login**

- Sign in doctor

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "doctor": {
            "username": "doctor_1",
            "password": "doctorpass"
        }
    }

**Response Payload:**

.. code::

    {
        "code": 1,
        "msg": "Successfully Signed In!"
    }
    
---------------------

**POST : http://Jason:secret@localhost:8081/api/v1.0/doctor/calendars**

- Add one calendar for doctor

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "calendar": {
            "summary": "Calendar for Patient - Tester",
            "description": "This is Calendar description",
            "location": "MARS",
            "timezone": "Australia/Melbourne",
            "customer_id": "2"
        }
    }

**Response Payload:**

.. code::

    {
        "code": 1,
        "data": {
            "calendar_id": "rmit.edu.au_jjp4pg3i54121j1dvqbq0bulg0@group.calendar.google.com",
            "doctor_id": 2
        },
        "msg": "Successfully Added!"
    }
    
---------------------

**GET : http://Jason:secret@localhost:8081/api/v1.0/doctor/all**

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
            }
        ],
        "msg": "Successfully Fetched!"
    }
    
---------------------


**GET : http://Jason:secret@localhost:8081/api/v1.0/doctor/1**

- Get one patient

**Headers:**

.. code::

    Content-Type : application/json

**Response Payload:**

.. code::

    {
        "code": 1,
        "data": {
            "age": 40,
            "calendar_id": "rmit.edu.au_6ch9mp71j3crcb9kdd0tit4u88@group.calendar.google.com",
            "created_at": "Sat, 29 Sep 2018 23:58:43 GMT",
            "email": "doctor1@maps.com",
            "id": 1,
            "name": "Lee",
            "password": "23d5c51afade7a8701186250777f3c055c94984ce3d4aaed11438c0c",
            "phone": "402358178",
            "sex": 2,
            "username": "doctor_1"
        },
        "msg": "Successfully Fetched!"
    }
    
---------------------


**POST : http://Jason:secret@localhost:8081/api/v1.0/doctor/calendars/rmit.edu.au_6ikss7t01v7hs7na036hedbdm8@group.calendar.google.com/events**

- Add a event in calendar

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "event": {
            "summary": "Event for Patient - Tester",
            "description": "This is Event description",
            "location": "MARS",
            "timezone": "Australia/Melbourne",
            "start": "2018-09-20T09:00:00-07:00",
            "end": "2018-09-21T09:00:00-07:00",
            "patient_email": "doctor1@maps.com",
            "doctor_email": "doctor1@maps.com"
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
                }
            ],
            "created": "2018-09-27T21:47:42.000Z",
            "creator": {
                "email": "s3620273@student.rmit.edu.au"
            },
            "description": "This is Event description",
            "end": {
                "dateTime": "2018-09-22T02:00:00+10:00",
                "timeZone": "Australia/Melbourne"
            },
            "etag": "\"3076169725105000\"",
            "htmlLink": "https://www.google.com/calendar/event?eid=dGZwbms1N2lnaTNxOG4xZzdqdDhsMGpsM28gcm1pdC5lZHUuYXVfNmlrc3M3dDAxdjdoczduYTAzNmhlZGJkbThAZw",
            "iCalUID": "tfpnk57igi3q8n1g7jt8l0jl3o@google.com",
            "id": "tfpnk57igi3q8n1g7jt8l0jl3o",
            "kind": "calendar#event",
            "location": "MARS",
            "organizer": {
                "displayName": "Calendar for doctor1@maps.com",
                "email": "rmit.edu.au_6ikss7t01v7hs7na036hedbdm8@group.calendar.google.com",
                "self": true
            },
            "reminders": {
                "overrides": [
                    {
                        "method": "popup",
                        "minutes": 10
                    },
                    {
                        "method": "email",
                        "minutes": 1440
                    }
                ],
                "useDefault": false
            },
            "sequence": 0,
            "start": {
                "dateTime": "2018-09-21T02:00:00+10:00",
                "timeZone": "Australia/Melbourne"
            },
            "status": "confirmed",
            "summary": "Event for Patient - Tester",
            "updated": "2018-09-27T21:47:42.603Z"
        },
        "msg": "Successfully added!"
    }
    
---------------------

**GET : http://Jason:secret@localhost:8081/api/v1.0/doctor/calendars/rmit.edu.au_0jctq4qp159m3j5oe0fqnaaue0@group.calendar.google.com/events**

- Get all events by calendar id

**Headers:**

.. code::

    Content-Type : application/json

**Response Payload:**

.. code::

    {
        "code": 1,
        "data": [
            {
                "attendees": [
                    {
                        "email": "info@maps.com",
                        "responseStatus": "needsAction"
                    },
                    {
                        "email": "doctor_2@maps.com",
                        "responseStatus": "needsAction"
                    },
                    {
                        "email": "patient_1@maps.com",
                        "responseStatus": "needsAction"
                    }
                ],
                "created": "2018-09-29T07:53:54.000Z",
                "creator": {
                    "email": "s3620273@student.rmit.edu.au"
                },
                "description": "Free Time",
                "end": {
                    "dateTime": "2018-10-01T04:00:00+10:00",
                    "timeZone": "Australia/Melbourne"
                },
                "etag": "\"3076415300785000\"",
                "htmlLink": "https://www.google.com/calendar/event?eid=amwxdGRwanJwYzQzM3NmYzE5bDFiZGlvdjAgcm1pdC5lZHUuYXVfMGpjdHE0cXAxNTltM2o1b2UwZnFuYWF1ZTBAZw",
                "iCalUID": "jl1tdpjrpc433sfc19l1bdiov0@google.com",
                "id": "jl1tdpjrpc433sfc19l1bdiov0",
                "kind": "calendar#event",
                "location": "MAPS",
                "organizer": {
                    "displayName": "Calendar for doctor_2@maps.com",
                    "email": "rmit.edu.au_0jctq4qp159m3j5oe0fqnaaue0@group.calendar.google.com",
                    "self": true
                },
                "reminders": {
                    "overrides": [
                        {
                            "method": "popup",
                            "minutes": 10
                        },
                        {
                            "method": "email",
                            "minutes": 1440
                        }
                    ],
                    "useDefault": false
                },
                "sequence": 0,
                "start": {
                    "dateTime": "2018-10-01T00:30:00+10:00",
                    "timeZone": "Australia/Melbourne"
                },
                "status": "confirmed",
                "summary": "Booked",
                "updated": "2018-09-29T07:54:26.070Z"
            },
            {
                "attendees": [
                    {
                        "email": "info@maps.com",
                        "responseStatus": "needsAction"
                    },
                    {
                        "email": "doctor_2@maps.com",
                        "responseStatus": "needsAction"
                    },
                    {
                        "displayName": "李捷",
                        "email": "mrjasonedu@gmail.com",
                        "responseStatus": "needsAction"
                    }
                ],
                "created": "2018-09-29T07:53:58.000Z",
                "creator": {
                    "email": "s3620273@student.rmit.edu.au"
                },
                "description": "Free Time",
                "end": {
                    "dateTime": "2018-10-03T05:00:00+10:00",
                    "timeZone": "Australia/Melbourne"
                },
                "etag": "\"3076415616560000\"",
                "htmlLink": "https://www.google.com/calendar/event?eid=NWVsdnB0NGV1ZDdmN2x0M25ydjJpNzVwa28gcm1pdC5lZHUuYXVfMGpjdHE0cXAxNTltM2o1b2UwZnFuYWF1ZTBAZw",
                "iCalUID": "5elvpt4eud7f7lt3nrv2i75pko@google.com",
                "id": "5elvpt4eud7f7lt3nrv2i75pko",
                "kind": "calendar#event",
                "location": "MAPS",
                "organizer": {
                    "displayName": "Calendar for doctor_2@maps.com",
                    "email": "rmit.edu.au_0jctq4qp159m3j5oe0fqnaaue0@group.calendar.google.com",
                    "self": true
                },
                "reminders": {
                    "overrides": [
                        {
                            "method": "popup",
                            "minutes": 10
                        },
                        {
                            "method": "email",
                            "minutes": 1440
                        }
                    ],
                    "useDefault": false
                },
                "sequence": 0,
                "start": {
                    "dateTime": "2018-10-03T02:00:00+10:00",
                    "timeZone": "Australia/Melbourne"
                },
                "status": "confirmed",
                "summary": "Booked",
                "updated": "2018-09-29T07:59:38.179Z"
            }
        ],
        "msg": "Successfully fetched!"
    } 
    
---------------------


**DELETE : http://Jason:secret@localhost:8081/api/v1.0/doctor/calendars/rmit.edu.au_qi0lao2o8lg50sgd8rhj8gqd64@group.calendar.google.com/events/hiuluadu4bbtb7msgamkp7n108**

- Delete one event

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

**GET : http://Jason:secret@localhost:8081/api/v1.0/doctor/email/doctor6@test.com**

- Get doctor by email

**Headers:**

.. code::

    Content-Type : application/json

**Response Payload:**

.. code::

    {
        "code": 1,
        "data": {
            "age": 30,
            "calendar_id": "rmit.edu.au_vej5mcqg523sfdf6r6vsapa7a0@group.calendar.google.com",
            "created_at": null,
            "email": "doctor6@test.com",
            "id": 7,
            "name": "Lee",
            "password": "23d5c51afade7a8701186250777f3c055c94984ce3d4aaed11438c0c",
            "phone": "402358178",
            "sex": 1,
            "username": "doctor6"
        },
        "msg": "Successfully Fetched!"
    }

---------------------

**GET : http://Jason:secret@localhost:8081/api/v1.0/doctor/appointments/2**

- Get appointment by appointment id

**Headers:**

.. code::

    Content-Type : application/json

**Response Payload:**

.. code::

    {
        "code": 1,
        "data": {
            "appointed_from": "2018-10-01T00:30:00",
            "appointed_to": "2018-10-01T02:30:00",
            "created_at": "2018-09-30T00:04:28+00:00",
            "diagnoses": "Test2",
            "doctor_id": 1,
            "google_calendar_id": "rmit.edu.au_6ch9mp71j3crcb9kdd0tit4u88@group.calendar.google.com",
            "google_event_id": "phnmmt9em0o2t78r9ig76hv44c",
            "id": 2,
            "notes": "Test1",
            "patient_id": 1
        },
        "msg": "Successfully Fetched!"
    }

---------------------

**GET : http://Jason:secret@localhost:8081/api/v1.0/doctor/1/appointments**

- Get appointment by appointment id

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
                "doctor_id": 1,
                "google_calendar_id": "rmit.edu.au_6ch9mp71j3crcb9kdd0tit4u88@group.calendar.google.com",
                "google_event_id": "phnmmt9em0o2t78r9ig76hv44c",
                "id": 2,
                "notes": "Test1",
                "patient": {
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
                "patient_id": 1
            },
            {
                "appointed_from": "2018-10-02T09:15:00",
                "appointed_to": "2018-10-02T09:30:00",
                "created_at": "2018-10-01T19:45:54+00:00",
                "diagnoses": "",
                "doctor_id": 1,
                "google_calendar_id": "rmit.edu.au_6ch9mp71j3crcb9kdd0tit4u88@group.calendar.google.com",
                "google_event_id": "9qdrl84ee8ojj4bjl6o6dqrhf8",
                "id": 15,
                "notes": "",
                "patient": {
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
                "patient_id": 1
            },
            {
                "appointed_from": "2018-09-28T02:30:00+10:00",
                "appointed_to": "2018-09-28T05:30:00+10:00",
                "created_at": "2018-09-21T21:15:00+00:00",
                "diagnoses": null,
                "doctor_id": 1,
                "google_calendar_id": "",
                "google_event_id": "",
                "id": 16,
                "notes": null,
                "patient": {
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
                "patient_id": 1
            }
        ],
        "msg": "Successfully Fetched!"
    }

--------------

**PUT : http://Jason:secret@localhost:8081/api/v1.0/doctor/appointments/8**

- Update appointment by id

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "appointment": {
            "notes": "test"
        }
    }

**Response Payload:**

.. code::

    {
        "code": 1,
        "msg": "Successfully Updated!"
    }