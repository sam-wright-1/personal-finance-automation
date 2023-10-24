"""Class to handle google sheet connection"""
import logging
import os
import pandas as pd

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

class GoogleSheetObject:
    """Class to handle Google Sheets"""
    
    def __init__(self, spreadsheet_id):
        """Init"""
        self.credentials = self.get_creds()
        self.spreadsheet_id = spreadsheet_id
        
    def get_creds(self):
        """Sets credentials (might need some manual acceptance)"""
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
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w", encoding="utf-8") as token:
                token.write(creds.to_json())
        
        return creds
    
    def get_google_service(self):
        """Getting google sheet service"""
        try:
            service = build("sheets", "v4", credentials=self.credentials)
        except HttpError as err:
            logging.info(err)
        # Call the Sheets API
        return service.spreadsheets()
    
    def get_google_sheet_data(self, sheet_range, google_sheet_headers:list):
        """Gets google sheet data"""

        result = (
            self.get_google_service().values()
            .get(spreadsheetId=self.spreadsheet_id, range=sheet_range)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return
        
        df = pd.DataFrame(values, columns=google_sheet_headers)
        
        return df.drop(index=df.index[0], axis=0, inplace=True)
    
    def update_google_sheets(self, updated_dataframe, start_range):
        """Take data and update the google sheet"""
        
        # Execute google sheet update
        logging.info(" Inserting %s rows.", {len(updated_dataframe)})
        
        new_list = updated_dataframe.values.tolist()
        update_values = self.get_google_service().values().update(
            spreadsheetId = self.spreadsheet_id,
            range=start_range,
            valueInputOption="RAW",
            body={"values": new_list},
        )
        update_values.execute()