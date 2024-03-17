from fastapi import HTTPException
import os.path
from google.oauth2.credentials import Credentials
from ..configs.calendar import SCOPES, CLIENT_TOKEN_FILE
from googleapiclient.discovery import build
from datetime import datetime
import pytz
from .. import schemas


async def get_credentials():
    credential = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(CLIENT_TOKEN_FILE):
        credential = Credentials.from_authorized_user_file(CLIENT_TOKEN_FILE, SCOPES)
    else:
        raise HTTPException(status_code=403, detail="Credential does not exist")
    return credential

async def insert_event(summary, description):
    credential = await get_credentials()
    service = build("calendar", "v3", credentials=credential)
    tz = pytz.timezone('Asia/Ho_Chi_Minh')
    date_now = str(datetime.now(tz).strftime('%Y-%m-%dT%H:%M:%S'))
    event = {
            'summary': summary,
            'description': description,
            'start': {
              'dateTime': date_now,
              'timeZone': 'Asia/Ho_Chi_Minh',
            },
            'end': {
              'dateTime': date_now,
              'timeZone': 'Asia/Ho_Chi_Minh',
            }
        }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return event.get('htmlLink')


async def create_event(data: schemas.calendar.JiraDataRequest):
    # data = data.model_dump() 
    issue_data = data['issue']['fields']
    project_data = issue_data['project']
    
    summary = project_data['name'] + ' ' + issue_data['summary']
    
    labels = ', '.join(issue_data['labels'])
    description = 'Priority: ' + issue_data['priority']['name'] + '\nLabel: ' + labels + '\nIssue: ' + data['issue']['self']
    
    result = await insert_event(summary, description)
    results = {}
    results['link'] = result
    return results