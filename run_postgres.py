#!/usr/bin/env python

import os
from dotenv import load_dotenv

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

# Add any additional commands or configurations as needed
# For example, you might want to wait for the PostgreSQL container to be ready
# before proceeding with other tasks. You can use tools like "wait-for-it" for this purpose.
# Check https://github.com/vishnubob/wait-for-it for more details.


# dont foget for : (bash)  chmod +x run_postgres.py
# chmod u+x run_postgres.py

# for run this file in bash:  ./run_postgres.py
