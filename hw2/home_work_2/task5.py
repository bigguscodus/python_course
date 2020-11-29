import string


def custom_range(*args):
    result = []
    for value in args[0]:
        result.append(value)
    print(result[result.index("p") : result.index(args[1])])
    return result[result.index("p") : result.index(args[1])]
