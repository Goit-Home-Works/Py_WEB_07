from typing import List
from datetime import datetime
from sqlalchemy import  String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


class Grade(Base):
    __tablename__ = "grade"
    id: Mapped[int] = mapped_column(primary_key=True)
    grade: Mapped[int] = mapped_column(nullable=False)
    date_of: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    student_id: Mapped[int] = mapped_column(
        ForeignKey("student.id", ondelete="CASCADE")
    )
    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subject.id", ondelete="CASCADE")
    )

    student: Mapped["Student"] = relationship("Student", back_populates="grade")
    subject: Mapped["Subject"] = relationship("Subject", back_populates="grades")


class Group(Base):
    __tablename__ = "group"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    students: Mapped["Student"] = relationship(
        "Student", back_populates="group", cascade="all, delete", passive_deletes=True
    )


class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column( nullable=False)
    last_name: Mapped[str] = mapped_column( nullable=False)
    email: Mapped[str]
    phone: Mapped[str]
    group_id: Mapped[int] = mapped_column(
        ForeignKey("group.id", ondelete="SET NULL"), nullable=True
    )

    group: Mapped["Group"] = relationship("Group", back_populates="students")
    grade: Mapped["Grade"] = relationship("Grade", back_populates="student")

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str]
    phone: Mapped[str]

    subjects: Mapped[List["Subject"]] = relationship(
        "Subject",
        back_populates="teacher",
        cascade="all, delete",
        passive_deletes=True,
    )

    @hybrid_property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"id={self.id}, fullname={self.full_name}, email={self.email}"


class Subject(Base):
    __tablename__ = "subject"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("teacher.id", ondelete="SET NULL"), nullable=True
    )

    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="subjects")
    grades: Mapped[List["Grade"]] = relationship("Grade", back_populates="subject")
