# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:21:19 2024

@author: dragon
"""

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import numpy as np
import pandas as pd

import madDictionary

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly","https://www.googleapis.com/auth/documents"]

# the dictionary and story list sheet.
MADLIB_SHEET_ID = "1GKVnudQK-5QdoxBpt2KceHg6ZooyMYwU7fWAVFAyouw"
WORDS = "Words!A1:z1000"
STORIES = "Stories!A1:z1000"

def getCreds():
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
    return creds

def getStoryByName(name):
    result = getGoogleSheet(MADLIB_SHEET_ID,STORIES)    
    values=result['values']
    df = pd.DataFrame(values)
    df.columns = df.iloc[0]
    df = df[1:]
    for index,row in df.iterrows():
        if row['storyname'] == name:
            return row['urlString']
    return None

def getStories():
    result = getGoogleSheet(MADLIB_SHEET_ID,STORIES)
    values=result['values']
    df = pd.DataFrame(values)
    df.columns = df.iloc[0]
    df = df[1:]
    return df.storyname
    
def getStory(docID):
    creds = getCreds()
    try:
        service = build("docs", "v1", credentials=creds)
        # Retrieve the documents contents from the Docs service.
        document = service.documents().get(documentId=docID, includeTabsContent=True).execute()
        return "".join(getTextTab(tab) for tab in document.get('tabs'))
    except HttpError as err:
        print(err)

def getTextTab(tab): 
    document = tab.get('documentTab')
    content = document.get('body').get('content')
    return read_structural_elements(content)
    return "".join(readStructuralElements(element) for element in content)

def getGoogleSheet(sheetID = MADLIB_SHEET_ID, sheetRange = WORDS): 
    creds = getCreds()
    try:
        service = build("sheets", "v4", credentials=creds)
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=sheetID, range=sheetRange)
            .execute()
        )
        return result
    except HttpError as err:
        print(err)
        return None

def getDictionary():
    result = getGoogleSheet(MADLIB_SHEET_ID,WORDS)
    values=result['values']
    df = pd.DataFrame(values)
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.replace('', np.nan)
    dictionary = madDictionary.MadDictionary(df)
    return dictionary

def read_paragraph_element(element):
  text_run = element.get('textRun')
  if not text_run:
    return ''
  return text_run.get('content')


def read_structural_elements(elements):
  text = ''
  for value in elements:
    if 'paragraph' in value:
      elements = value.get('paragraph').get('elements')
      for elem in elements:
        text += read_paragraph_element(elem)
    elif 'table' in value:
      table = value.get('table')
      for row in table.get('tableRows'):
        cells = row.get('tableCells')
        for cell in cells:
          text += read_structural_elements(cell.get('content'))
    elif 'tableOfContents' in value:
      # The text in the TOC is also in a Structural Element.
      toc = value.get('tableOfContents')
      text += read_structural_elements(toc.get('content'))
  return text
