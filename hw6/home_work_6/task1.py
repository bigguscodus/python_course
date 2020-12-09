def instances_counter(cls):
    setattr(cls, "instances_created", 0)
    orig_init = cls.__init__

    def new_init(self, *args, **kwargs):
        orig_init(self, *args, **kwargs)
        self.__class__.instances_created += 1

    def _get_created_instances():
        return cls.instances_created

    def _reset_instances_counter():
        temp_result = cls.instances_created
        cls.instances_created = 0
        return temp_result

    setattr(cls, "__init__", new_init)
    setattr(cls, "get_created_instances", _get_created_instances)
    setattr(cls, "reset_instances_counter", _reset_instances_counter)
    return cls
