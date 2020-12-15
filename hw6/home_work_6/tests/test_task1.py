from home_work_6.task1 import instances_counter


def test_instances_counter():
    @instances_counter
    class User:
        pass

    User.get_created_instances()
    user, _, _ = User(), User(), User()
    assert User.get_created_instances() == 3
    User.reset_instances_counter()
    assert User.get_created_instances() == 0
