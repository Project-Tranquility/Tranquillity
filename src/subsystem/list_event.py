import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.subsystem.get_creds import get_creds
from datetime import datetime as normaldatetime
from zoneinfo import ZoneInfo

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/gmail.readonly",]


def format_event_time(iso_string: str) -> str:
    if "T" not in iso_string:
        # événement toute la journée, pas d'heure
        return iso_string
    dt_utc = normaldatetime.fromisoformat(iso_string.replace("Z", "+00:00"))
    dt_paris = dt_utc.astimezone(ZoneInfo("Europe/Paris"))
    return dt_paris.strftime("%Y-%m-%d %H:%M")

def list_calendar(number: int):
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = get_creds()
  
  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=number,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return ""

    content = []
    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(format_event_time(start), event["summary"])
      temp_content = f"{start} - {event["summary"]}"
      content.append(temp_content)
    return "\n".join(content)

  except HttpError as error:
    print(f"An error occurred: {error}")

if __name__ == "__main__":
  list_calendar(5)