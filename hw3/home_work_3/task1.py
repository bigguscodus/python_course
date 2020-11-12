from collections.abc import Callable


def cache(times) -> Callable:
    def decorator(func):
        cache_house = []
        def wrapper(*args):
            for stored_args, result in cache_house:
                if stored_args == args:
                    return result
            result = func(*args)
            cache_house.append((args, result))
            return result
        return wrapper
    return decorator

@cache(times=2)
def f():
    return input('? ')

f()
f()
f()
f()
