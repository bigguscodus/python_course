import itertools
import math
from collections import deque
from collections.abc import Sequence
from typing import List, Tuple


def _is_perfect_square(number: int) -> bool:
    square = int(math.sqrt(number))
    return square * square == number


def _is_fibonacci_number(number: int) -> bool:
    return _is_perfect_square(5 * number * number + 4) or _is_perfect_square(
        5 * number * number - 4
    )  # math magic


def check_fibonacci(data: Sequence) -> bool:
    """Accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

    :param data: A Sequence of integers
    :return: A True or False
    """
    for _ in data:
        if _is_fibonacci_number(_):
            continue
        else:
            return False
    return True


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Reads input line-by-line, and find maximum and minimum values.

    :param file_name: path to the file
    :return: A tuple with maximum and minimum values
    """
    total_values = list()
    with open(file_name) as fi:
        for line in fi:
            total_values.extend([int(_) for _ in line.split(" ")])
    sorted_total_values = sorted(total_values)
    return sorted_total_values[0], sorted_total_values[-1]


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
    Works with O(N^4), be careful

    :param a: List of integers
    :param b: List of integers
    :param c: List of integers
    :param d: List of integers
    :return: Integer number os zero sums
    """
    total_list = [a, b, c, d]
    counter = 0
    for _ in itertools.product(
        *total_list
    ):  # maybe this is not algorythmically effective, but i am too lazy
        if sum(_) != 0:
            continue
        else:
            counter += 1
    return counter


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """find a sub-array with length less equal to "k", with maximal sum.

    :param nums: list of integers
    :param k: maximum size of the window
    :return: Maximum sum of the subarray"""
    result = 0
    for window_size in range(1, k + 1):
        subarray = deque(nums[:window_size])
        if sum(subarray) > result:
            result = sum(subarray)
        for _ in nums[window_size:]:
            subarray.popleft()
            subarray.append(_)
            if sum(subarray) > result:
                result = sum(subarray)
    return result
