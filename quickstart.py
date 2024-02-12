# add 3 after pip if u have pip3 version
# Install in terminal -> pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#Added to get full content
from base64 import urlsafe_b64decode
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Labels
INBOX = "INBOX"
CHAT = "CHAT"
SENT = "SENT"
IMPORTANT = "IMPORTANT"
TRASH = "TRASH"
DRAFT = "DRAFT"
SPAM = "SPAM"
CATEGORY_FORUMS = "CATEGORY_FORUMS"
CATEGORY_UPDATES = "CATEGORY_UPDATES"
CATEGORY_PERSONAL = "CATEGORY_PERSONAL"
CATEGORY_PROMOTIONS = "CATEGORY_PROMOTIONS"
CATEGORY_SOCIAL = "CATEGORY_SOCIAL"
STARRED = "STARRED"
UNREAD = "UNREAD"


def extractEmails(service, label_id):
    try:
        # Call the Gmail API
        # Retrieve messages from given label

        results = service.users().messages().list(userId="me", labelIds=[label_id]).execute()
        messages = results.get("messages", [])

        # Retrieve and print the content of each message
        for message in messages:
            msg = service.users().messages().get(userId="me", id=message["id"], format='full').execute()
            

            headers = msg["payload"]["headers"]
            # Find the subject header in the email headers
            subject = next((header["value"] for header in headers if header["name"] == "Subject"), "Subject not found")
            from_email = next((header["value"] for header in headers if header["name"].lower() == "from"), "Sender not found")
            date = next((header["value"] for header in headers if header["name"].lower() == "date"), "Date not found")
            print(f"Subject: {subject}")
            print(f"From: {from_email}")
            print(f"Date: {date}")
            print("Message ID:", message["id"])
            # Print whole content
            part = msg['payload']
            body = ""
            if part['mimeType'] == 'text/plain' or part['mimeType'] == 'text/html':
                body = urlsafe_b64decode(part['body']['data'].encode('ASCII')).decode('utf-8')
            else:
                # Handling multipart/alternative and others
                for subpart in part.get('parts', []):
                    if subpart['mimeType'] == 'text/plain' or subpart['mimeType'] == 'text/html':
                        body = urlsafe_b64decode(subpart['body']['data'].encode('ASCII')).decode('utf-8')
                        break
            
            print("Message Content:", body)
            print("\n")

    except HttpError as error:
        # TODO: Handle errors from Gmail API.
        print(f"An error occurred: {error}")


def main():
    # Creates List of the user's Gmail labels.

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        results = service.users().labels().list(userId="me").execute()
        labels = results.get("labels", [])

        if not labels:
            print("No labels found.")
            return
        print("Labels:")

        for label in labels:

            # Extract emails from Inbox
            if label["name"] == INBOX:
                extractEmails(service, label["id"])
                break

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
