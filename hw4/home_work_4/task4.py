from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    For any number in range n replacing any number divisible by three with the word "fizz",
    and any number divisible by five with the word "buzz".
    >>> fizzbuzz(5)
    [1, 2, 'fizz', 4, 'buzz']
    """
    result = [] * n
    for fizzbuzz in range(1, n + 1):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            result.append("fizz buzz")
        elif fizzbuzz % 3 == 0:
            result.append("fizz")
        elif fizzbuzz % 5 == 0:
            result.append("buzz")
        else:
            result.append(fizzbuzz)
    return result
