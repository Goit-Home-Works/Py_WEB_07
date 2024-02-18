#!/bin/bash
import os
from dotenv import load_dotenv


DB_NAME = os.getenv("DB_NAME")
DB_HOST =  os.getenv("DB_HOST")
DB_PASSWORD =  os.getenv("DB_PASSWORD")
IMAGE_NAME =  os.getenv("IMAGE_NAME")


docker run --name DB_NAME -p DB_HOST:DB_HOST -e POSTGRES_PASSWORD=DB_PASSWORD -d IMAGE_NAME

# Add any additional commands or configurations as needed
# For example, you might want to wait for the PostgreSQL container to be ready
# before proceeding with other tasks. You can use tools like "wait-for-it" for this purpose.
# Check https://github.com/vishnubob/wait-for-it for more details.


# dont foget for : (bash)  chmod +x run_postgres.sh

# for run this file in bash:  ./run_postgres.sh
