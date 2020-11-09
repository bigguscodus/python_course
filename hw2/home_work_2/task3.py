import itertools
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    result = []
    for i in itertools.product(*args):
        result.append(list(i))
    return result
