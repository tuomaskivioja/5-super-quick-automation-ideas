import os
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# ! Specify the ID of the folder to upload files to (from the URL of the Drive folder)
folder_id = ''

SCOPES=['https://www.googleapis.com/auth/drive']


def create_connection():

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

# define a function to upload a file to Google Drive
def upload_file(file_path, file_name, creds):

    service = build('drive', 'v3', credentials=creds)
    try:
        # create a MediaFileUpload object for the file
        file = MediaFileUpload(file_path, resumable=True)

        # create a file resource with metadata
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }

        # send a request to upload the file
        file = service.files().create(
            body=file_metadata,
            media_body=file,
            fields='id'
        ).execute()

        print(f'File "{file_name}" uploaded to Google Drive with ID: {file.get("id")}')

    except HttpError as error:
        print(f'An error occurred while uploading file "{file_name}" to Google Drive: {error}')
        file = None

    return file

# define a function to bulk upload files to Google Drive
def upload_files(directory_path, creds):
    # get the list of files in the directory
    files = os.listdir(directory_path)

    # iterate over each file and upload it to Google Drive
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        upload_file(file_path, file_name, creds)

# example usage
creds = create_connection()
# ! Fill in the path to the folder you want to upload files from (from your local computer)
directory_path = ''
upload_files(directory_path, creds)