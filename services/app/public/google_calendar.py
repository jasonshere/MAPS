from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os

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

# add event
def addGoogleEvent(data):
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

# get events
def getGoogleEvents(calendar_id):
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

# delete event
def deleteGoogleEvent(calendar_id, event_id):
    try:
        service.events().delete(calendarId = calendar_id, eventId = event_id).execute()
        return True, {}
    except Exception as e:
        return False, e
