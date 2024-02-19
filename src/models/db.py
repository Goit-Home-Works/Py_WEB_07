import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Get environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

print(f"DB_USER: {DB_USER}")
print(f"DB_PASSWORD: {DB_PASSWORD}")
print(f"DB_HOST: {DB_HOST}")
print(f"DB_PORT: {DB_PORT}")
print(f"DB_NAME: {DB_NAME}")

# Constructing URI
uri = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(f"Constructed URI: {uri}")

# Read configuration from config.ini
file_config = Path(__file__).parent.parent.parent.joinpath("config.ini")
print(file_config)
config = configparser.ConfigParser()
config.read(file_config)

# Get values from config.ini
username = config.get("DB", "USER")
password = config.get("DB", "PASSWORD")
domain = config.get("DB", "DOMAIN")
db_name = config.get("DB", "DATABASE")

# Constructing URI from config.ini
url = f"postgresql://{username}:{password}@{domain}:5432/{db_name}"
print(f"Constructed URI from config.ini: {url}")


def get_engine():
    if uri:
        engine = create_engine(uri, echo=True)
        DBsession = sessionmaker(bind=engine)
        session = DBsession()
        return engine, session, uri
    return None, None, None

engine = create_engine(url, echo=False)

DBSession = sessionmaker(bind=engine)
session = DBSession()
