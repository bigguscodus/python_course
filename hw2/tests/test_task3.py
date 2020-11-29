import pytest
from home_work_2.task3 import combinations


def test_combinations():
    actual_result = combinations([1, 2], [3, 4])

    assert actual_result == [[1, 3], [1, 4], [2, 3], [2, 4]]
