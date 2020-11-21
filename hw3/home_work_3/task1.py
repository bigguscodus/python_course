from collections.abc import Callable


def cache(times) -> Callable:
    def decorator(func):
        cache_house = {}
        count_of_caching = {}
        def wrapper(*args, **kwargs):
            rest_times = count_of_caching.get(args, 0)
            if rest_times < 1:
                cache_house[args] = func(*args, **kwargs)
                count_of_caching[args] = times
            else:
                count_of_caching[args] -= 1
            return cache_house[args]

        return wrapper
    return decorator
