"""
Configuration file
"""
import os

from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
if not SQLALCHEMY_DATABASE_URI:
    raise Exception("Database URI not specified")
SQLALCHEMY_TRACK_MODIFICATIONS = True
ALL_RECORDS_CSV_FILENAME = "records.csv"
