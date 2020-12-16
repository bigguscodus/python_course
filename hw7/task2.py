def _grid_interpritator(string_with_grid: str):
    temp_result = []
    for index, value in enumerate(list(string_with_grid)):
        if value == "#":
            continue
        try:
            if string_with_grid[index + 1] == "#":
                continue
            else:
                temp_result.append(value)
        except IndexError:
            temp_result.append(value)
    return temp_result


def backspace_compare(first: str, second: str) -> bool:
    return _grid_interpritator(first) == _grid_interpritator(second)
