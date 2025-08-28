# import the packages
import os, warnings, logging
import pandas as pd

from oauth2client.service_account import ServiceAccountCredentials
import gspread

logging.basicConfig(
    level = logging.INFO,
    format = '[%(levelname)s] %(asctime)s — %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)


def gsheet_upload(
        gsheet_credentials: str, 
        spreadsheet_id: str, 
        worksheet_name: str, 
        upload_df: pd.DataFrame) -> None:
    """
    Upload a pandas DataFrame to a Google Sheet (full replace).

    Parameters:
        gsheet_credentials (str): Path to the Service Account JSON key file.
        spreadsheet_id (str): Spreadsheet ID of the target spreadsheet.
        worksheet_name (str): Worksheet name of the target worksheet in the target spreadsheet.
        upload_df (str): Dataframe to upload.

    Returns:
        None

    Raises:
        TypeError: If the input path is not a DOCX file.
    """

    try:

        # read the Google Sheet credentials
        creds = ServiceAccountCredentials.from_json_keyfile_name(gsheet_credentials, ["https://www.googleapis.com/auth/spreadsheets"])
    
        # connect to the Google Sheet
        client = gspread.authorize(creds)
    
        # loacate to the google sheet
        spreadsheet = client.open_by_key(spreadsheet_id)
        worksheet = spreadsheet.worksheet(worksheet_name)
    
        # clean the original data
        worksheet.clear()

        # upload data
        worksheet.update([upload_df.columns.values.tolist()] + upload_df.values.tolist(), value_input_option = "USER_ENTERED")
        
        # log reminder
        logging.info(f"The dataset has been uploaded to Google Sheet: {spreadsheet.title}.{worksheet_name}")

    # error check    
    except gspread.exceptions.SpreadsheetNotFound as e:
        raise RuntimeError(f"Google Sheet ID <{spreadsheet_id}> invalid or no permission.") from e
    
    except gspread.exceptions.WorksheetNotFound as e:
        raise RuntimeError(f"Google Sheet tab <{worksheet_name}> not found.") from e    
    
    except TypeError as e:
        if "not JSON serializable" in str(e):
            raise TypeError("The dataset contains values that are not JSON-serializable.") from e
        raise
        
    except gspread.exceptions.APIError as e:
        raise RuntimeError(f"Google Sheet API error: {e}") from e


