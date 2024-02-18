from alembic.config import Config
from alembic import command
from models.db import get_engine


# Function to run migration
def run_migration():
    # Get a database engine using your function
    engine, _, _ = get_engine()

    # Path to your Alembic configuration file
    alembic_cfg = "./alembic.ini"

    # Alembic configuration
    config = Config(alembic_cfg)
    config.set_main_option("sqlalchemy.url", str(engine.url))

    # Create migration for "Create teacher table"
    command.revision(config, autogenerate=True, message="Create teacher table")

    # Create migration for "Create users models"
    command.revision(config, autogenerate=True, message="Create users models")

    # Apply migrations to the database
    command.upgrade(config, "head")


if __name__ == "__main__":
    run_migration()
