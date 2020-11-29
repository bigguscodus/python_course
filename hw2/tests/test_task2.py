import pytest
from home_work_2.task2 import major_and_minor_elem


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [([3, 2, 3], (3, 2)), ([2, 2, 1, 1, 1, 2, 2], (2, 1))],
)
def test_major_and_minor_elem(value, expected_result):
    actual_result = major_and_minor_elem(value)

    assert actual_result == expected_result
