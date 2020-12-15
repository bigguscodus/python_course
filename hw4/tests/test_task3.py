from home_work_4.task3 import my_precious_logger


def test_my_precious_logger(capfd):
    my_precious_logger("OK")
    my_precious_logger("error use R instead of Python")
    out, err = capfd.readouterr()
    assert out == "OK"
    assert err == "error use R instead of Python"
