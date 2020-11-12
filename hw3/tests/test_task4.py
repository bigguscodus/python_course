import pytest

from home_work_3.task4 import is_armstrong

@pytest.mark.parametrize(
    ["value", "expected_result"],
    [(1,True), (153,True), (10, False)]
)
def test_is_armstsstrong(value, expected_result):
    actual_result = is_armstrong(value)

    assert actual_result == expected_result