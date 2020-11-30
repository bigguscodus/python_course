import pytest
from home_work_1.hw1 import (
    check_fibonacci,
    check_sum_of_four,
    find_maximal_subarray_sum,
    find_maximum_and_minimum,
)


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [([0, 1, 1], True), ([10, 20], False)],
)
def test_check_fibonacci(value, expected_result):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result


def test_find_maximum_and_minimum():
    actual_result = find_maximum_and_minimum("test_file.txt")

    assert actual_result == (1, 8)


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [([0], [0], [1], [-1], 1), ([0, 1, 2], [0, 1, 2], [0, -1, -2], [0, -1, 2], 14)],
)
def test_check_sum_of_four(a, b, c, d, expected_result):
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([0, 1, 2, 3, 4, 5, 0], 3, 12),
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-1, -1, -1, 100], 3, 100),
    ],
)
def test_find_maximal_subarray_sum(nums, k, expected_result):
    actual_result = find_maximal_subarray_sum(nums, k)

    assert actual_result == expected_result
