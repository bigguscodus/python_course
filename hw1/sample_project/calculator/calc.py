import math


def check_power_of_2(a: int) -> bool:
    if a < 0 or a == 0 or a == 1:
        return False
    return math.log(a, 2).is_integer()
