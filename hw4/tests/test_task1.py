import os

import pytest
from home_work_4.task1 import read_magic_number


@pytest.fixture()
def create_positive_test_file():
    file_name = "positive_test_file.txt"
    with open(file_name, "w+") as file:
        file.write("2")
    yield file_name
    os.remove(file_name)


def test_read_magic_number_positive(create_positive_test_file):
    actual_result = read_magic_number(create_positive_test_file)

    assert actual_result


def test_read_magic_number_negative():
    with pytest.raises(ValueError):
        read_magic_number("not_existed_file.txt")
