import os
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Get environment variables
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")
IMAGE_NAME = os.getenv("IMAGE_NAME")
DB_PORT = os.getenv("DB_PORT")

# Construct the docker run command
docker_run_command = f"docker run --name {DB_NAME} -p {DB_PORT}:{DB_PORT} -e POSTGRES_PASSWORD={DB_PASSWORD} -d {IMAGE_NAME}"

# Run the docker command
os.system(docker_run_command)

# Add a delay to wait for PostgreSQL to initialize (adjust the sleep time as needed)
time.sleep(10)
print("Wait...")
time.sleep(5)

# Continue with database creation
create_db_command = f"createdb -h {DB_HOST} -p {DB_PORT} -U postgres {DB_NAME}"
os.system(create_db_command)

# dont foget for : (bash)  chmod +x run_postgres.py
# chmod u+x run_postgres.py

# for run this file in bash:  ./run_postgres.py
