import re
import sys


def my_precious_logger(text: str):
    if bool(re.match("^error", text)):
        sys.stderr.write(text)
    else:
        sys.stdout.write(text)
