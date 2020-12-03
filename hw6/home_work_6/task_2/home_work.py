import datetime


class HomeWork:
    def __init__(self, text: str, deadline: int, solution: int):
        self.text, self.deadline, self.solution = (
            text,
            datetime.timedelta(days=deadline),
            solution,
        )
        self.created = datetime.datetime.now()

    def is_active(self):
        print(datetime.datetime.now())
        print(self.created)
        print(self.deadline)
        print(datetime.datetime.now() - self.created < self.deadline)
        return datetime.datetime.now() - self.created < self.deadline


class HomeworkResult:
    def __init__(self, author, task: HomeWork, solution: str):
        if isinstance(task, HomeWork) == False:
            raise TypeError("You gave a not Homework object")
        self.homework = task
        self.created, self.solution, self.author = task.created, solution, author
