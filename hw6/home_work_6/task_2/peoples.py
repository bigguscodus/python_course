from collections import defaultdict

from home_work_6.task_2.exceptions import DeadlineError
from home_work_6.task_2.home_work import HomeWork, HomeworkResult


class SchoolParticipants:
    def __init__(self, last_name: str, first_name: str):
        self.last_name, self.first_name = last_name, first_name


class Student(SchoolParticipants):
    def do_homework(self, home_work: HomeWork, solution) -> HomeworkResult:
        if not home_work.is_active():
            raise DeadlineError("You are late")
        return HomeworkResult(self, home_work, solution)


class Teacher(SchoolParticipants):
    homework_done = defaultdict(set)

    @classmethod
    def create_homework(cls, text: str, deadline: int) -> HomeWork:
        return HomeWork(text, deadline, None)

    @classmethod
    def check_homework(cls, home_work_result: HomeworkResult) -> bool:
        if len(home_work_result.solution) < 5:
            return False
        return True

    @classmethod
    def reset_results(cls, homework=None) -> defaultdict:
        if homework:
            del cls.homework_done[homework]
        else:
            cls.homework_done.clear()
        return cls.homework_done
