import datetime


class HomeWork:
    def __init__(self, text: str, deadline: int):
        self.text, self.deadline = text, datetime.timedelta(deadline)
        self.created = datetime.date.today()

    def is_active(self):
        return datetime.date.today() < self.created + self.deadline


class Student:
    def __init__(self, last_name: str, first_name: str):
        self.last_name, self.first_name = last_name, first_name

    def do_homework(self, home_work: HomeWork):
        if home_work.is_active():
            return home_work
        print("You are late")
        return None


class Teacher:
    def __init__(self, last_name: str, first_name: str):
        self.last_name, self.first_name = last_name, first_name

    def create_homework(self, text, deadline):
        return HomeWork(text, deadline)


if __name__ == "__main__":
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    print(teacher.last_name)  # Daniil
    print(student.first_name)  # Petrov

    expired_homework = teacher.create_homework("Learn functions", 0)
    print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
    print(expired_homework.deadline == datetime.timedelta(0))  # 0:00:00
    print(expired_homework.text)  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
