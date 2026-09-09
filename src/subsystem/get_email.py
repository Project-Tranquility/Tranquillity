import requests
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
import html2text
from src.subsystem.get_creds import get_creds

def get_header(payload, name):
    for h in payload["headers"]:
        if h["name"].lower() == name.lower():
            return h["value"]
    return ""

def html_to_text(html_content: str) -> str:
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.body_width = 0
    return h.handle(html_content).strip()

def get_body(payload):
    plain_text = None
    html_text = None

    if "parts" in payload:
        for part in payload["parts"]:
            # gère aussi les parts imbriquées (multipart/alternative dans multipart/mixed)
            if part.get("parts"):
                nested = get_body(part)
                if nested:
                    return nested
            if part["mimeType"] == "text/plain" and not plain_text:
                data = part["body"].get("data")
                if data:
                    plain_text = base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
            elif part["mimeType"] == "text/html" and not html_text:
                data = part["body"].get("data")
                if data:
                    html_text = base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
    else:
        data = payload.get("body", {}).get("data")
        if data:
            decoded = base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
            if payload.get("mimeType") == "text/html":
                html_text = decoded
            else:
                plain_text = decoded

    if plain_text and plain_text.strip():
        return plain_text.strip()
    if html_text:
        return html_to_text(html_text)
    return ""

def get_email(number: int):
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  creds = get_creds()
  try:
    # Call the Gmail API and limit the result to the requested number of emails.
    service = build("gmail", "v1", credentials=creds)
    results = (
        service.users().messages().list(
            userId="me", labelIds=["INBOX"], maxResults=number
        ).execute()
    )
    messages = results.get("messages", [])

    if not messages:
        print("No messages found.")
        return

    print("Messages:")
    content = []
    for message in messages:
        print(f'Message ID: {message["id"]}')
        msg = (
            service.users().messages().get(
                userId="me", id=message["id"], format="full"
            ).execute()
        )
        subject = get_header(msg["payload"], "Subject")
        date = get_header(msg["payload"], "Date")
        sender = get_header(msg["payload"], "From")
        body = get_body(msg["payload"])
        print(sender)
        print(date)
        print(subject)
        print(body)
        content.append(f"Sender : {sender}.\n Date : {date}.\n Subject: {subject}.\n Body: {body}\n")
    return "\n".join(content)
        

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")