import sys
import os

from sqlalchemy import select, delete

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from models.db import session
from models.models import Grade, Student, Subject, Group

from faker import Faker
from datetime import date, datetime
from random import randint, choice
import logging

package_name = "hw"
logger = logging.getLogger(f"{package_name}.{__name__}")
fake = Faker()

TOTAL_GRADES_DAYS = 400


def erase_grades():
    # deleted_grades = session.query(Grade).delete()
    deleted_grades = session.execute(delete(Grade))
    logger.info(f"{deleted_grades=}")


def select_groups():
    return session.execute(select(Group.id)).all()
    # return session.query(Group).all()


def select_students():
    return session.execute(select(Student.id)).all()
    #return session.query(Student).all()


def select_students_in_group(group_id: int):
    return session.execute(select(Student.id).filter_by(group_id=group_id)).all()
    #return session.query(Student).filter_by(group_id=group_id).all()


def select_subjects():
    return session.execute(select(Subject.id)).all()
    # return session.query(Subject.id).all()


def get_random_day() -> date:
    satrt_date = datetime.strptime("2023-04-21", "%Y-%m-%d")
    end_date = datetime.strptime("2024-02-20", "%Y-%m-%d")

    fake_day: date
    while True:
        fake_day = fake.date_between(satrt_date, end_date)
        if fake_day.isoweekday() < 6:
            break
    return fake_day


def create_grades(total: int = TOTAL_GRADES_DAYS):
    groups = select_groups()
    if not groups:
        logger.error("GROUPS NOT FOUND")
        return
    students = select_students()
    if not students:
        logger.error("students NOT FOUND")
        return
    subjects = select_subjects()
    if not subjects:
        logger.error("subjects NOT FOUND")
        return

    erase_grades()
    grade_day = 0
    while True:
        random_subject = choice(subjects).id
        group_id = choice(groups).id
        group_students = select_students_in_group(group_id)
        group_students_id = [st.id for st in group_students]
        max_random_students_in_group = min(12, len(group_students))
        min_random_students_in_group = min(3, len(group_students))
        # random_student = choice(select_students_in_group(group_id)).id
        random_date_of = get_random_day()
        how_many_grades_today_in_group = randint(
            min_random_students_in_group, max_random_students_in_group
        )
        for _ in range(how_many_grades_today_in_group):
            random_grade = randint(30, 100)
            random_student = choice(group_students_id)
            grade = Grade(
                grade=random_grade,
                student_id=random_student,
                subject_id=random_subject,
                date_of=random_date_of,
            )
            session.add(grade)
        grade_day += 1
        if grade_day >= total:
            break
    session.commit()
    logger.info(f"{grade_day=}")


# def seed_grade():
#     satrt_date = datetime.strptime("2023-04-21", "%Y-%m-%d")
#     end_date = datetime.strptime("2024-02-20", "%Y-%m-%d")

#     def get_day() -> date:
#         fake_day: date
#         while True:
#             fake_day = fake.date_between(satrt_date, end_date)
#             if fake_day.isoweekday() < 6:
#                 break
#         return fake_day

#     grades = []
#     sql = "INSERT INTO grade(grade, subjects_id, students_id, date_of) VALUES (?, ?, ?, ?);"
#     for _ in range(TOTAL_GRADES):
#         random_subject = randint(1, len(subjects))
#         random_group = randint(1, len(groups))
#         # random_grads = [randint(1, TOTAL_grads) for _ in range(randint(3, 12))]
#         group_grads = get_group_grads(cur, random_group)
#         max_random_grads_in_group = min(12, len(group_grads))
#         min_random_grads_in_group = min(3, len(group_grads))
#         random_grads = sample(
#             group_grads,
#             randint(min_random_grads_in_group, max_random_grads_in_group),
#         )
#         # random_grads = []
#         random_date_of = get_day()
#         for random_student in random_grads:
#             random_grade = randint(30, 100)
#             grades.append(
#                 (random_grade, random_subject, random_student, random_date_of)
#             )
#     try:
#         cur.executemany(sql, grades)
#     except Error as e:
#         logger.error(e)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.ERROR)
    # logger.setLevel(logging.INFO)
    create_grades()
