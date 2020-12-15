from unittest.mock import MagicMock

import pytest
from home_work_4.task2 import count_dots_on_i


def test_count_dots_on_i_negative():
    count_dots_on_i = MagicMock(
        side_effect=ValueError("Unreachable https://example.com/")
    )
    with pytest.raises(ValueError, match="Unreachable https://example.com/"):
        count_dots_on_i("https://example.com/")


def test_count_dots_on_i_positive():
    actual_result = count_dots_on_i("https://example.com/")

    assert actual_result == 59
