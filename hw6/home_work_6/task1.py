def instances_counter(cls):
    setattr(cls, "instances_created", 0)

    def __init__(self):
        cls.instances_created += 1

    def _get_created_instances():
        return cls.instances_created

    def _reset_instances_counter():
        temp_result = cls.instances_created
        cls.instances_created = 0
        return temp_result

    setattr(cls, "__init__", __init__)
    setattr(cls, "get_created_instances", _get_created_instances)
    setattr(cls, "reset_instances_counter", _reset_instances_counter)
    return cls


@instances_counter
class User:
    pass


print(User.get_created_instances())
user, _, _ = User(), User(), User()
print(User.get_created_instances())
