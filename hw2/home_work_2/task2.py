from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    most_common_item = Counter(inp).most_common()
    return most_common_item[0][0], most_common_item[-1][0]
