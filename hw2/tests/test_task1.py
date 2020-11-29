import pytest
from home_work_2.task1 import (
    _count_chars,
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def test_get_longest_diverse_words():
    actual_result = get_longest_diverse_words("test_data2.txt")

    assert "q" not in actual_result


def test_get_rarest_char():
    actual_result = get_rarest_char("test_data.txt")

    assert actual_result == "#"


def test_count_punctuation_chars():
    actual_result = count_punctuation_chars("test_data.txt")

    assert actual_result == 8301


def test_count_non_ascii_chars():
    actual_result = count_non_ascii_chars("test_data.txt")

    assert actual_result == 54810


def test_get_most_common_non_ascii_char():
    actual_result = get_most_common_non_ascii_char("test_data.txt")

    assert actual_result == " "
