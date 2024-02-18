import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from models.db import session
from models.models import Student, Group


from faker import Faker
import random
import logging

package_name="hw"
logger = logging.getLogger(f"{package_name}.{__name__}")

TOTAL_students = 100


def erase_students():
    deleted_students = session.query(Student).delete()
    logger.info(f"{deleted_students=}")


def select_groups():
    return session.query(Group).all()


def create_students(total: int = TOTAL_students):
    groups = select_groups()
    if not groups:
        logger.error("GROUPS NOT FOUND")
        return

    fake: Faker = Faker("uk-UA")
    erase_students()
    for _ in range(total):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address(),
            group_id=random.choice(groups).id,
        )
        session.add(student)
    session.commit()


if __name__ == "__main__":
    logging.basicConfig()
    logger.setLevel(logging.INFO)       
    create_students()
