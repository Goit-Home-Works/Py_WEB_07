from alembic.config import Config
from alembic import command
from models.db import get_engine


# Function to run migration
def run_migration():
    # Path to your Alembic configuration file
    alembic_cfg = "./alembic.ini"

    # Alembic configuration
    config = Config(alembic_cfg)

    # Create migration for "Create teacher table"
    command.revision(config, autogenerate=True, message="Create teacher table")

    # Create migration for "Create users models"
    command.revision(config, autogenerate=True, message="Create users models")

    # Apply migrations to the database
    command.upgrade(config, "head")


if __name__ == "__main__":
    run_migration()
