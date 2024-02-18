from datetime import datetime
import faker
from random import randint, choice
from sqlalchemy import select

from models import Group, Student, Professor, Grade, Subject
from db import session

NUMBER_STUDENTS = 50
NUMBER_PROFESSORS = 5
NUMBER_SUBJECTS = 5
NUMBER_GRADES = 19
FAKE_SUBJECTS = [
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
FAKE_GROUPS = ["001", "002", "003"]

fake_data = faker.Faker()


def seed_groups() -> None:

    for name in FAKE_GROUPS:
        session.add(Group(group_name=name))
    session.commit()


def seed_students():
    for _ in range(NUMBER_STUDENTS):
        session.add(
            Student(student_name=fake_data.name(), group_id=choice(FAKE_GROUPS))
        )
    session.commit()


def seed_professors():
    for _ in range(NUMBER_PROFESSORS):
        session.add(Professor(professor_name=fake_data.name()))
    session.commit()


def seed_subjects():
    for name in FAKE_SUBJECTS:
        session.add(
            Subject(subject_name=name, professor_id=randint(1, NUMBER_PROFESSORS))
        )
    session.commit()


def seed_grades():
    for stud in range(1, NUMBER_STUDENTS + 1):
        for _ in range(NUMBER_GRADES):
            session.add(
                Grade(
                    student_id=stud,
                    subject_id=randint(1, NUMBER_SUBJECTS),
                    grade=randint(50, 100),
                    date_recieved=datetime(
                        randint(2022, 2023), randint(1, 12), randint(1, 28)
                    ).date(),
                )
            )
    session.commit()


if __name__ == "__main__":
    with session as session:
        seed_groups()
        seed_students()
        seed_professors()
        seed_subjects()
        seed_grades()
