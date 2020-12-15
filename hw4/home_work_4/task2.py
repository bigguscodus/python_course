import urllib.request


def count_dots_on_i(url: str) -> int:
    try:
        request_result = urllib.request.urlopen(url)
        result = 0
        for line in request_result:
            result += line.decode().count("i")
        return result
    except Exception:
        raise ValueError(f"Unreachable {url}")
