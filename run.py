import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

def import_favorite_data(spreadsheet_name):
    try:
        spreadsheet = GSPREAD_IMPORT.open(spreadsheet_name)
        foodworksheet = spreadsheet.get_worksheet(0)
        srrveydata = foodworksheet.get_all_survey_records()

      