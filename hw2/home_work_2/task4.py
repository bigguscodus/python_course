from collections.abc import Callable


def cache(func: Callable) -> Callable:
    cache_house = {}

    def wrapper(*args):
        if args in cache_house:
            return cache_house[args]
        else:
            computed_result = func(*args)
            cache_house[args] = computed_result
            return computed_result

    return wrapper
