import functools


def fancy_naming(original_func, doc, name):
    def fancy_naming(func):
        func.__original_func = original_func
        func.__name__ = name
        func.__doc__ = doc
        return func

    return fancy_naming


def print_result(func):
    @fancy_naming(func, func.__doc__, func.__name__)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    without_print = custom_sum.__original_func

    # the result returns without printing
    without_print(1, 2, 3, 4)
