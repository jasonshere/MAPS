Clerk Endpoints
---------------------------------

.. code::

    This module contains all of Clerk module endpoints.
    In order to be able to request endpoints, you need to use auth user
    The Test user and password are : Jason:secret

**The supports of Clerk model**

- Support to register a clerk account
- Support to Sign in the MAPS with a clerk account
- Support to fetch appointments Of doctors


**Endpoints**

**POST : http://Jason:secret@localhost:8081/api/v1.0/clerk/register**

- Add a new clerk account

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "clerk": {
            "username": "clerk_1",
            "email": "clerk_1@maps.com",
            "password": "clerk_pass",
            "name": "clerk3",
            "phone": "+610403456789",
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
        "msg": "Successfully created!"
    }


**POST : http://Jason:secret@localhost:8081/api/v1.0/clerk/login**

- Sign in clerk

**Headers:**

.. code::

    Content-Type : application/json

**Request Payload:**

.. code::

    {
        "clerk": {
            "username": "clerk_1",
            "password": "clerkpass"
        }
    }

**Response Payload:**

.. code::

    {
        "code": 1,
        "msg": "Successfully Signed In!"
    }

**GET : http://Jason:secret@localhost:8081/api/v1.0/doctor/1/appointments**

- Get all appointments of specific doctor

**Headers:**

.. code::

    Content-Type : application/json

**Response Payload:**

.. code::

    {
        "code": 1,
        "msg": "Successfully Signed In!"
    }

**GET : http://Jason:secret@localhost:8081/api/v1.0/clerk/statistics**

- Get all appointment data of doctor for statistics

**Headers:**

.. code::

    Content-Type : application/json


**Response Payload:**

.. code::

    {
        "code": 1,
        "data": {
            "appointments": {
                "Doctor_1": [
                    3,
                    1,
                    0,
                    1,
                    0,
                    1,
                    0
                ],
                "Lee": [
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0
                ]
            },
            "labels": [
                "2018-09-30",
                "2018-10-01",
                "2018-10-02",
                "2018-10-03",
                "2018-10-04",
                "2018-10-05",
                "2018-10-06"
            ]
        },
        "msg": "Successfully Fetched!"
    }

**GET : http://Jason:secret@localhost:8081/api/v1.0/clerk/statistics**

- Get all appointment data of all doctors

**Headers:**

.. code::

    Content-Type : application/json


**Response Payload:**

.. code::

    {
        "code": 1,
        "data": [
            {
                "age": 20,
                "appointments": {
                    "count": 2,
                    "data": [
                        {
                            "attendees": [
                                {
                                    "displayName": "李捷",
                                    "email": "mrjasonedu@gmail.com",
                                    "responseStatus": "needsAction"
                                },
                                {
                                    "email": "test@test.com",
                                    "responseStatus": "needsAction"
                                }
                            ],
                            "created": "2018-09-23T09:37:51.000Z",
                            "creator": {
                                "email": "s3620273@student.rmit.edu.au"
                            },
                            "description": "This is Event description",
                            "end": {
                                "dateTime": "2018-09-24T02:00:00+10:00",
                                "timeZone": "Australia/Melbourne"
                            },
                            "etag": "\"3075390944251000\"",
                            "htmlLink": "https://www.google.com/calendar/event?eid=aG9ybTU2cWgwdGRzb3F1Z2M5b29jc2sxY2sgcm1pdC5lZHUuYXVfcWkwbGFvMm84bGc1MHNnZDhyaGo4Z3FkNjRAZw",
                            "iCalUID": "horm56qh0tdsoqugc9oocsk1ck@google.com",
                            "id": "horm56qh0tdsoqugc9oocsk1ck",
                            "kind": "calendar#event",
                            "location": "MARS",
                            "organizer": {
                                "displayName": "Calendar for Patient - Tester",
                                "email": "rmit.edu.au_qi0lao2o8lg50sgd8rhj8gqd64@group.calendar.google.com",
                                "self": true
                            },
                            "reminders": {
                                "overrides": [
                                    {
                                        "method": "email",
                                        "minutes": 1440
                                    },
                                    {
                                        "method": "popup",
                                        "minutes": 10
                                    }
                                ],
                                "useDefault": false
                            },
                            "sequence": 0,
                            "start": {
                                "dateTime": "2018-09-23T02:00:00+10:00",
                                "timeZone": "Australia/Melbourne"
                            },
                            "status": "confirmed",
                            "summary": "Event for Patient - Tester",
                            "updated": "2018-09-23T09:37:52.333Z"
                        },
                        {
                            "attendees": [
                                {
                                    "displayName": "李捷",
                                    "email": "mrjasonedu@gmail.com",
                                    "responseStatus": "needsAction"
                                },
                                {
                                    "email": "test@test.com",
                                    "responseStatus": "needsAction"
                                }
                            ],
                            "created": "2018-09-23T09:38:30.000Z",
                            "creator": {
                                "email": "s3620273@student.rmit.edu.au"
                            },
                            "description": "This is Event description",
                            "end": {
                                "dateTime": "2018-09-22T02:00:00+10:00",
                                "timeZone": "Australia/Melbourne"
                            },
                            "etag": "\"3075391020886000\"",
                            "htmlLink": "https://www.google.com/calendar/event?eid=OXVpYTZzdnVpdjdmYTk1cTltY3IzanRoaHMgcm1pdC5lZHUuYXVfcWkwbGFvMm84bGc1MHNnZDhyaGo4Z3FkNjRAZw",
                            "iCalUID": "9uia6svuiv7fa95q9mcr3jthhs@google.com",
                            "id": "9uia6svuiv7fa95q9mcr3jthhs",
                            "kind": "calendar#event",
                            "location": "MARS",
                            "organizer": {
                                "displayName": "Calendar for Patient - Tester",
                                "email": "rmit.edu.au_qi0lao2o8lg50sgd8rhj8gqd64@group.calendar.google.com",
                                "self": true
                            },
                            "reminders": {
                                "overrides": [
                                    {
                                        "method": "email",
                                        "minutes": 1440
                                    },
                                    {
                                        "method": "popup",
                                        "minutes": 10
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
                            "updated": "2018-09-23T09:38:30.540Z"
                        }
                    ]
                },
                "calendar_id": "rmit.edu.au_qi0lao2o8lg50sgd8rhj8gqd64@group.calendar.google.com",
                "created_at": "2018-09-09T21:00:00+00:00",
                "email": "test2@test2.com",
                "id": 1,
                "name": "doctor",
                "password": "23d5c51afade7a8701186250777f3c055c94984ce3d4aaed11438c0c",
                "phone": "123123123",
                "sex": 1,
                "username": "test2"
            },
            {
                "age": 20,
                "appointments": {
                    "count": 0,
                    "data": []
                },
                "calendar_id": "rmit.edu.au_675eo74292fe4g2e4hu2eqjh1c@group.calendar.google.com",
                "created_at": "2018-09-09T21:00:00+00:00",
                "email": "test3@test2.com",
                "id": 2,
                "name": "doctor3",
                "password": "23d5c51afade7a8701186250777f3c055c94984ce3d4aaed11438c0c",
                "phone": "123123123",
                "sex": 1,
                "username": "test3"
            }
        ],
        "msg": "Successfully Fetched!"
    }