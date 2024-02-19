from datetime import datetime

from sqlalchemy import String
from .db import engine

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql.schema import ForeignKey


class Base(DeclarativeBase):
    pass


# Table: groups
class Group(Base):
    __tablename__ = "groups"
    group_id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str] = mapped_column(String(10))
    students_list: Mapped[list["Student"]] = relationship(back_populates="group")


# Table: students
class Student(Base):
    __tablename__ = "students"
    student_id: Mapped[int] = mapped_column(primary_key=True)
    student_name: Mapped[str] = mapped_column(String(50))
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.group_id"))
    group: Mapped["Group"] = relationship("Group", back_populates="students_list")


# Table: professors
class Professor(Base):
    __tablename__ = "professors"
    professor_id: Mapped[int] = mapped_column(primary_key=True)
    professor_name: Mapped[str] = mapped_column(String(50))


# Table subjects
class Subject(Base):
    __tablename__ = "subjects"
    subject_id: Mapped[int] = mapped_column(primary_key=True)
    subject_name: Mapped[str] = mapped_column(String(25), unique=True)
    professor_id: Mapped[int] = mapped_column(ForeignKey("professors.professor_id"))
    professor: Mapped["Professor"] = relationship("Professor", backref="subjects")


# Table grades
class Grade(Base):
    __tablename__ = "grades"
    grade_id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.student_id"))
    student: Mapped["Student"] = relationship("Student", backref="grades")
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.subject_id"))
    subject: Mapped["Subject"] = relationship("Subject", backref="grades")
    grade: Mapped[int] = mapped_column()
    date_recieved: Mapped[datetime] = mapped_column()
 
def create_tables():
    Base.metadata.drop_all(engine, checkfirst=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

if __name__ == "__main__":
    create_tables()