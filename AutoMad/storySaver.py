# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:44:54 2024

@author: dragon
"""

import os.path
import random

import numpy as np
import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly","https://www.googleapis.com/auth/documents"]
SAVEDOC = "1Oha700Q9R_gGvVT2G2NYdL8Ixpr0xGwNVDJ3jMWOOhI"

def saveStory(story):
    story=story.replace("<br>","\n")+"\n\n\n"
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
        requests = [
            {
                'insertText': {
                    'text': story,
                    'endOfSegmentLocation': {}
                    }
                }
            ]
        service = build('docs', 'v1', credentials=creds)
        results = service.documents().batchUpdate(documentId=SAVEDOC, body={'requests': requests}).execute()
        print(results)
    except HttpError as err:
        print(err)
        return None

