# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:44:54 2024

@author: dragon
"""

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import wordGrabber

SAVEDOC = "1Oha700Q9R_gGvVT2G2NYdL8Ixpr0xGwNVDJ3jMWOOhI"

def saveStory(story):
    story=story.replace("<br>","\n")+"\n\n\n"
    creds = wordGrabber.getCreds()
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
    except HttpError as err:
        print(err)
        return None

