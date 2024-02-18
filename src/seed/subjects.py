import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import random
import logging


from models.db import session
from models.models import Subject
from models.models import Teacher


package_name="hw"
logger = logging.getLogger(f"{package_name}.{__name__}")

SUBJECTS = [
    "Python Core",
    "Python Web",
    "Python Data Science",
    "HTML CSS",
    "Soft Skils",
    "Databases SQL, noSQL",
    "English",
    "Git",
    "Computer repair",
    "Web design",
]


def erase_subjects():
    deleted_subjects = session.query(Subject).delete()
    logger.info(f"{deleted_subjects=}")


def select_teachers():
    return session.query(Teacher).all()


def create_subjects():
    teachers = select_teachers()
    if not teachers:
        logger.error("Teachers NOT FOUND")
        return
    erase_subjects()
    for subject_name in SUBJECTS:
        subject = Subject(
            name=subject_name,
            teacher_id=random.choice(teachers).id
        )
        session.add(subject)
    session.commit()


if __name__ == "__main__":
    create_subjects()
