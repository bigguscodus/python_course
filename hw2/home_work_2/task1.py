import string
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    result = []
    with open(file_path) as file:
        for line in file:
            temp_line = [
                word for word in line.split(" ") if len(word) == len(set(word))
            ]
            temp_line.sort(key=lambda s: len(s), reverse=True)
            for word in temp_line:
                if word in result:
                    continue
                else:
                    if len(result) <= 9:
                        result.append(word)
                    else:
                        result.sort(key=lambda s: len(s))
                        for value in result:
                            if len(value) < len(word):
                                result[result.index(value)] = word
                                break
    return result


def _count_chars(file_path):
    result = {}
    with open(file_path) as file:
        for line in file:
            for symbol in line:
                if symbol not in result:
                    result[symbol] = 1
                else:
                    result[symbol] += 1
    return result


def get_rarest_char(file_path: str) -> str:
    temp_result = _count_chars(file_path)
    value_count = list(temp_result.items())
    value_count.sort(key=lambda x: x[1])
    return value_count[0][0]


def count_punctuation_chars(file_path: str) -> int:
    temp_result = _count_chars(file_path)
    result = 0
    for char in string.punctuation:
        try:
            result += temp_result[char]
        except KeyError:
            continue
    return result


def count_non_ascii_chars(file_path: str) -> int:
    temp_result = _count_chars(file_path)
    result = 0
    for char in temp_result:
        if char in string.ascii_letters:
            continue
        else:
            result += temp_result[char]
    return result


def get_most_common_non_ascii_char(file_path: str) -> str:
    temp_result = _count_chars(file_path)
    non_ascii_chars = {
        key: value
        for key, value in temp_result.items()
        if key not in string.ascii_letters
    }
    value_count = list(non_ascii_chars.items())
    value_count.sort(key=lambda x: x[1])
    return value_count[-1][0]
