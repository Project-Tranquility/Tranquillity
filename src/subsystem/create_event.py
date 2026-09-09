# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/workspace/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.
from googleapiclient.discovery import build
from src.subsystem.get_creds import get_creds

def create_event(title: str, description: str, startTime: str, endTime: str):
    """
    Summary:
        Create a event in your google calendar
    Args: 
        title: just a title
        description: just a description
        startTime: start of your event like this '2026-09-09T09:00:00-07:00'
        endTime: same type of startTime
    """
    creds = get_creds()
    service = build("calendar", "v3", credentials=creds)
    event = {
      'summary': title,
      'location': 'None',
      'description': description,
      'start': {
        'dateTime': startTime,
        'timeZone': 'Europe/Paris',
      },
      'end': {
        'dateTime': endTime,
        'timeZone': 'Europe/Paris',
      },
      'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=1'
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
    return "'Event created: %s' % (event.get('htmlLink'))"

