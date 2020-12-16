from hw7.task3 import tic_tac_toe_checker


def test_tic_tac_toe_checker_returns_x():
    example = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(example) == "x wins!"


def test_tic_tac_toe_checker_returns_o():
    example = [["-", "-", "o"], ["-", "o", "o"], ["o", "x", "x"]]
    assert tic_tac_toe_checker(example) == "o wins!"


def test_tic_tac_toe_checker_returns_x():
    example = [["-", "-", "o"], ["-", "o", "o"], ["-", "x", "x"]]
    assert tic_tac_toe_checker(example) == "unfinished"
