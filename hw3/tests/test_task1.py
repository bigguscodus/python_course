from unittest.mock import MagicMock

from home_work_3.task1 import cache


def test_count_calling_caching_object():
    mock = MagicMock()

    @cache(times=2)
    def f():
        mock()

    f()
    assert mock.call_count == 1  # put to cache
    f()
    assert mock.call_count == 1  # take from cache
    f()
    assert mock.call_count == 1  # take from cache
    f()
    assert mock.call_count == 2  # not from cache
