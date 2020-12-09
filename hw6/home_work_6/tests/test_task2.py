import pytest

from home_work_6.task_2.exceptions import DeadlineError
from home_work_6.task_2.home_work import HomeWork, HomeworkResult
from home_work_6.task_2.peoples import Student, Teacher


def test_do_homework_returns_homework_result():
    opp_teacher = Teacher("Daniil", "Shadrin")
    good_student = Student("Lev", "Sokolov")
    docs_hw = opp_teacher.create_homework("Read docs", 5)
    result_1 = good_student.do_homework(docs_hw, "A+ work")

    assert isinstance(result_1, HomeworkResult)


def test_do_homework_raises_deadline_error():
    opp_teacher = Teacher("Daniil", "Shadrin")
    lazy_student = Student("Rotman", "Petrov")
    oop_hw = opp_teacher.create_homework("Learn OOP", 0)
    with pytest.raises(DeadlineError):
        lazy_student.do_homework(oop_hw, "too late")


def test_class_initalisation():
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Rotman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)
    assert opp_teacher.first_name == "Shadrin"
    assert lazy_student.last_name == "Roman"
    assert isinstance(oop_hw, HomeWork)
    result_1 = good_student.do_homework(docs_hw, "A+ work")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2
