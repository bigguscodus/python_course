def read_magic_number(path: str) -> bool:
    try:
        with open(path) as file:
            first_line = file.readline()
            if 1.0 <= float(first_line) < 3.0:
                return True
            else:
                return False
    except Exception:
        raise ValueError
