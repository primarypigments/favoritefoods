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
        spreadsheet = GSPREAD_CLIENT.open(spreadsheet_name)

