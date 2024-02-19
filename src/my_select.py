from models.db import session
from sqlalchemy import asc, desc
from sqlalchemy import select, func
from models.models import Grade, Group, Student, Subject, Professor
from pprint import pprint


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    result = (
        session.query(
            Student.student_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.student_id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return result


# Знайти студента із найвищим середнім балом з певного предмета
def select_2():
    result = (
        session.query(
            Student.student_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .filter(Subject.subject_name == "Python Web")
        .join(Student)
        .join(Subject)
        .group_by(Student.student_id)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )
    return result


# Знайти середній бал у групах з певного предмета.
def select_3():
    result = (
        session.query(
            Group.group_id,
            Group.group_name,
            Subject.subject_name,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Subject)
        .join(Student)
        .join(Group)
        .filter(Subject.subject_name == "Databases SQL, noSQL")
        .group_by(Group.group_id)
        .group_by(Subject.subject_name)
        .order_by(asc(Group.group_id))
        .all()
    )
    return result


# Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4():
    result = (
        session.query(
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .all()
    )
    return result


# Знайти які курси читає певний викладач.
def select_5():
    result = (
        session.query(
            Professor.professor_id, Professor.professor_name, Subject.subject_name
        )
        .select_from(Professor)
        .join(Subject)
        .filter(Professor.professor_id == 2)
        .all()
    )
    return result


# Знайти список студентів у певній групі.
def select_6():
    result = (
        session.query(
            Group.group_id, Group.group_name, Student.student_id, Student.student_name
        )
        .select_from(Group)
        .join(Student)
        .filter(Group.group_id == 3)
        .all()
    )
    return result


# Знайти оцінки студентів у окремій групі з певного предмета
def select_7():
    result = (
        session.query(
            Group.group_id,
            Group.group_name,
            Subject.subject_name,
            Student.student_name,
            Grade.grade,
        )
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .join(Group)
        .filter(Group.group_id == 1)
        .filter(Subject.subject_name == "Web design")
        .all()
    )
    return result


# Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(professor_id=None):
    query = (
        session.query(
            Subject.subject_name,
            Professor.professor_id,
            func.round(func.avg(Grade.grade), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Subject)
        .join(Professor)
        .group_by(Subject.subject_name, Professor.professor_id)
    )
    if professor_id is not None:
        query = query.filter(Professor.professor_id == professor_id)

    result = query.all()
    return result


# Знайти список курсів, які відвідує певний студент.
def select_9():
    result = (
        session.query(Student.student_name, Subject.subject_name)
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .filter(Student.student_id == 8)
        .group_by(Student.student_name, Subject.subject_id)
        .all()
    )
    return result


# Список курсів, які певному студенту читає певний викладач
def select_10():
    result = (
        session.query(
            Student.student_id,
            Student.student_name,
            Professor.professor_id,
            Professor.professor_name,
            Subject.subject_name,
        )
        .select_from(Grade)
        .join(Subject)
        .join(Professor)
        .join(Student)
        .filter(Student.student_id == 10)
        .filter(Professor.professor_id == 3)
        .group_by(Student.student_id, Subject.subject_id, Professor.professor_id)
        .all()
    )
    return result


# Середній бал, який певний викладач ставить певному студентові.
def select_11(student_id=None, professor_id=None):
    query = (
        session.query(
            Student.student_name.label("student"),
            Professor.professor_name.label("professor"),
            func.round(func.avg(Grade.grade), 2).label("average_grade"),
        )
        .join(Grade, Student.student_id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.subject_id)
        .join(Professor, Subject.professor_id == Professor.professor_id)
        .group_by(
            Student.student_name,
            Professor.professor_name,
            Student.student_id,
            Professor.professor_id,
        )
        .order_by(Student.student_name, Professor.professor_name)
    )

    if student_id is not None:
        query = query.filter(Student.student_id == student_id)

    if professor_id is not None:
        query = query.filter(Professor.professor_id == professor_id)

    result = query.all()
    return result


# Grades of students in a certain group in a certain subject in the last lesson.


def select_12(group_id=None, subject_name=None):

    ranked_grades = (
        session.query(
            Group.group_name.label("group"),
            Subject.subject_name.label("subject"),
            Student.student_name.label("student"),
            Grade.grade,
            Grade.date_recieved,
            func.row_number()
            .over(
                partition_by=(
                    Subject.subject_name,
                    Group.group_name,
                    Student.student_name,
                ),
                order_by=desc(Grade.date_recieved),
            )
            .label("rnk"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .join(Group)
        .filter(Group.group_id == group_id, Subject.subject_name == subject_name)
        .cte("RankedGrades")
    )

    # Main query selecting from the CTE
    query = (
        session.query(
            ranked_grades.c.group,
            ranked_grades.c.subject,
            ranked_grades.c.student,
            ranked_grades.c.grade,
            ranked_grades.c.date_recieved,
        )
        .filter(ranked_grades.c.rnk == 1)
        .group_by(
            ranked_grades.c.group,
            ranked_grades.c.subject,
            ranked_grades.c.student,
            ranked_grades.c.grade,
            ranked_grades.c.date_recieved,  # Fix the column name here
        )
        .order_by(desc(ranked_grades.c.grade))
    )
    result = query.all()

    return result


if __name__ == "__main__":

    print(
        "--- QUERY 01 ---\n 5 students with the highest average score in all subjects:"
    )
    pprint(select_1())

    print(
        "\n",
        "--- QUERY 02 ---\n the student with the highest average score in Python Web:",
    )
    pprint(select_2())

    print("\n", "--- QUERY 03 ---\n average score in Databases SQL, noSQL in groups:")
    pprint(select_3())

    print("\n", "--- QUERY 04 ---\n average grade:")
    pprint(select_4())

    print("\n", "--- QUERY 05 ---\n subject of professor with ID=2")
    pprint(select_5())

    print("\n", "--- QUERY 06 ---\n students from the group with ID=3")
    pprint(select_6())

    print(
        "\n",
        "--- QUERY 07 ---\n grades in Web design of students of the group with ID=1",
    )
    pprint(select_7())

    print("\n", "--- QUERY 08 ---\n average grade gave by professor with ID=2")
    pprint(select_8(professor_id=2))

    print("\n", "--- QUERY 09 ---\n subjects of student with ID=8")
    pprint(select_9())

    print(
        "\n",
        "--- QUERY 10 ---\n list of subjects taught by the professor with ID=3 to a student with ID=10",
    )
    pprint(select_10())

    print(
        "\n",
        "--- QUERY 11 ---\n The average score given by a particular teacher to a particular student.",
    )
    pprint(select_11(student_id=19, professor_id=2))

    print(
        "\n",
        "--- QUERY 12 ---\n Grades of students in a certain group in a certain subject in the last lesson.",
    )
    group_id = 1
    subject_name = "Python Web"
    pprint(select_12(group_id, subject_name))
