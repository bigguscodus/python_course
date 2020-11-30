import pytest

from home_work_5.task1 import HomeWork, Student, Teacher


def test_classes_init():
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")

    assert teacher.first_name == "Daniil"
    assert student.last_name == "Petrov"


def test_integration_with_homework():
    student = Student("Roman", "Petrov")
    teacher = Teacher("Daniil", "Shadrin")
    test_homework = teacher.create_homework("Learn functions", 0)

    assert test_homework.text == "Learn functions"
    assert student.do_homework(test_homework) == "You are late"
