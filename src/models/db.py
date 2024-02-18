import os
from dotenv import load_dotenv
from pathlib import Path
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

package_name = "hw7"
logger = logging.getLogger(package_name)

# Завантаження змінних середовища з файлу .env
load_dotenv()

# Отримання значень змінних середовища
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

def get_engine():
    if uri:
        engine = create_engine(uri, echo=True)
        DBsession = sessionmaker(bind=engine)
        session = DBsession()
        return engine, session, uri
    return None, None, None


engine, session, uri = get_engine()
logger.debug("session created")

if not engine:
    logger.error("engine not created")
