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
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
        # https://realpython.com/pandas-dataframe/#:~:text=The%20pandas%20DataFrame%20is%20a,with%20in%20Excel%20or%20Calc.
        pdf = pd.DataFrame(surveydata)
        return pdf
        # https://www.youtube.com/watch?v=5RSYum-EWw4 explains "except Exception as e"
        except Exception as e:
        print(f"Error importing survey data: {e}")

      