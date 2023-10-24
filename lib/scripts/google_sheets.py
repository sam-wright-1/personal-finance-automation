import os

import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from lib.scripts.transform import transform_financial_data

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ""
SAMPLE_RANGE_NAME = "sheetname!A1:Z"

# Google Sheet Headers
HEADERS = [
    "Type",
    "Date",
    "Amount",
    "Description",
    "Individual",
    "Month",
    "Year",
    "Day",
    "Flow",
    "Notes",
]


def google_sheets_upload():
    """Shows basic usage of the Sheets API. Prints values from a sample spreadsheet."""

    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Construct the full path to the credentials file
    creds_file_path = os.path.join(parent_dir, "creds", "credentials.json")
    token_file_path = os.path.join(parent_dir, "creds", "token.json")

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_file_path):
        creds = Credentials.from_authorized_user_file(token_file_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_file_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file_path, "w", encoding="utf-8") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        # Set into Dataframe
        df = pd.DataFrame(values, columns=HEADERS)
        df.drop(index=df.index[0], axis=0, inplace=True)
        df["Amount"] = pd.to_numeric(df["Amount"])
        df["Month"] = df["Month"].astype(int)
        df["Year"] = df["Year"].astype(int)
        # df['Individual'] = df['Indivu'].astype(int)

        start = str(len(df) + 2)
        start_range = f"sheetname!A{start}:Z"

        # Transforms savings, checking, citi files
        new_df = transform_financial_data()

        # dedup things
        merged_df = df.merge(
            new_df,
            on=HEADERS[:-1],
            how="right",
            indicator=True,
        )
        # Exclude rows that are in df2
        excluded_df = merged_df[merged_df["_merge"] == "right_only"]
        # Drop the indicator column
        excluded_df = excluded_df.drop(columns=["_merge", "Notes"]).sort_values(
            by=["Date"], ascending=True
        )

        # Execute google sheet update
        print(f" Inserting {len(excluded_df)} rows.")
        new_list = excluded_df.values.tolist()
        update_values = sheet.values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=start_range,
            valueInputOption="RAW",
            body={"values": new_list},
        )
        update_values.execute()

        print("Google Sheets have been updated")
    except HttpError as err:
        print(err)


if __name__ == "__main__":
    google_sheets_upload()
