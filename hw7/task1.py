from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    def _finder(tree=tree, search_target=element, count=None):
        if count is None:
            count = []
        if isinstance(tree, dict):
            for key, value in tree.items():
                _finder(value, search_target, count)
        elif hasattr(tree, "__iter__") and not isinstance(tree, str):
            for item in tree:
                _finder(item, search_target, count)
        elif isinstance(tree, str) and tree == search_target:
            count.append(search_target)
        return len(count)

    return _finder()
