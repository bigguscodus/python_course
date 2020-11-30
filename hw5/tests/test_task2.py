import pytest

from home_work_5.task2 import custom_sum, fancy_naming, print_result


def test_fancy_naming():

    actual_func = custom_sum(1, 2, 3, 4)
    actual_doc = custom_sum.__doc__
    actual_name = custom_sum.__name__

    assert actual_func == 10
    assert actual_doc == "This function can sum any objects which have __add___"
    assert actual_name == "custom_sum"
