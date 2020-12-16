from hw7.task2 import backspace_compare


def test_backspace_compare_returns_true():
    assert backspace_compare("ab#c", "ad#c") == True


def test_backspace_compare_returns_false():
    assert backspace_compare("a#c", "b") == False


def test_backsapce_corner_case():
    assert backspace_compare("####", "") == True
