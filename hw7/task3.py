from typing import List


def _rows(board):
    yield from board
    yield [board[i][i] for i in range(len(board))]


def lines(board):
    yield from _rows(board)
    yield from _rows(list(zip(*reversed(board))))


def tic_tac_toe_checker(board: List[List]) -> str:
    possible_results = {"x": "x wins!", "o": "o wins!", "-": "unfinished"}
    for line in lines(board):
        if len(set(line)) == 1 and line[0] != "#":
            return possible_results[line[0]]
    return possible_results["-"]
