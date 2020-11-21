import hashlib
import multiprocessing as mp
import random
import struct
import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


if __name__ == "__main__":
    pool = mp.Pool(50)
    results = pool.map(slow_calculate, [value for value in range(501)])
    pool.close()
