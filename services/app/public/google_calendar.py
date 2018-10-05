from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os
import datetime
import time
import math

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(os.path.abspath(os.path.dirname(__file__)) + '/credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# insert secondary calendar
def addSecondaryCalendar(summary, description, location, timezone):
    """
    add a secondary calendar
    :param summary: title
    :param description: description
    :param location: location
    :param timezone: timezone
    :return: boolean,object
    """
    try:
        calendar = {
            'summary': summary,
            'location': location,
            'description': description,
            'timeZone': timezone
        }
        created_calendar = service.calendars().insert(body=calendar).execute()
        return True, created_calendar['id']
    except Exception as e:
        return False, e

# set Freetime event
def setFreeTimeGoogleEvent(data):
    """
    set free time for doctor
    :param data: data
    :return: boolean,object
    """
    try:
        event = {
            'summary': data['summary'],
            'location': data['location'],
            'description': data['description'],
            'start': data['start'],
            'end': data['end'],
            'attendees': [
                {'email': data['doctor_email']},
                {'email': data['patient_email']},
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        event = service.events().insert(calendarId=data['calendar_id'], body=event).execute()
        return True, event
    except Exception as e:
        return False, e

# add event
def addGoogleEvent(data):
    """
    get google event
    :param data: data
    :return: boolean,object
    """
    try:
        start = time.mktime(time.strptime(data['start']['dateTime'], '%Y-%m-%dT%H:%M:%S'))
        end = time.mktime(time.strptime(data['end']['dateTime'], '%Y-%m-%dT%H:%M:%S'))
        n = math.ceil((end - start) / (15 * 60))
        for i in range(n):
            print(time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(int(start))), time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(int(start + (i + 1) * 15 * 60))))
            start1 = {
                'dateTime': time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(int(start + i * 15 * 60))),
                'timeZone': 'Australia/Melbourne'
            }
            end1 = {
                'dateTime': time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(int(start + (i + 1) * 15 * 60))),
                'timeZone': 'Australia/Melbourne'
            }
            print(start1, end1)
            event = {
                'summary': data['summary'],
                'location': data['location'],
                'description': data['description'],
                'start': start1,
                'end': end1,
                'attendees': [
                    {'email': data['doctor_email']},
                    {'email': data['patient_email']},
                ],
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'email', 'minutes': 24 * 60},
                        {'method': 'popup', 'minutes': 10},
                    ],
                },
            }
            print(event)
            event = service.events().insert(calendarId=data['calendar_id'], body=event).execute()
        
        return True, event
    except Exception as e:
        print(str(e))
        return False, e

# get events
def getGoogleEvents(calendar_id):
    """
    get all google events
    :param calendar_id: calendat id
    :return: boolean,object
    """
    try:
        page_token = None
        results = []
        while True:
            events = service.events().list(calendarId = calendar_id, pageToken = page_token).execute()
            for event in events['items']:
                results.append(event)
            page_token = events.get('nextPageToken')
            if not page_token:
                break
        return True, results
    except Exception as e:
        return False, e

# update events
def updateGoogleEvents(calendar_id, event_id, payload):
    """
    update google events
    :param calendar_id: calendar id
    :param event_id: event id
    :param payload: payload
    :return: boolean,object
    """
    try:
        # First retrieve the event from the API.
        event = service.events().get(calendarId=calendar_id, eventId=event_id).execute()
        event['summary'] = payload['summary']
        if payload['delete'] == "false":
            event['attendees'].append({'email': payload['email']})
        else:
            for item in event['attendees']:
                if item['email'] == payload['email']:
                    event['attendees'].remove(item)
        updated_event = service.events().update(calendarId=calendar_id, eventId=event['id'], body=event).execute()
        return True, updated_event
    except Exception as e:
        return False, e

# delete event
def deleteGoogleEvent(calendar_id, event_id):
    """
    delete google event
    :param calendar_id: calendar id
    :param event_id: event id
    :return: boolean,object
    """
    try:
        service.events().delete(calendarId = calendar_id, eventId = event_id).execute()
        return True, {}
    except Exception as e:
        return False, e
