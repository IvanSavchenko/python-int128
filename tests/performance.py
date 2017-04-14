"""Performance testing for int128 library."""

from __future__ import absolute_import

import timeit


setup = """

import random
import int128


NUMBER = random.randint(1, ((1 << 128) - 1))
BYTES = int128.to_bytes(NUMBER)

def to_bytes_c():
    int128.to_bytes(NUMBER, 'big')

def to_bytes_p():
    int128._to_bytes(NUMBER, 'big')

def from_bytes_c():
    int128.from_bytes(_BYTES)

def from_bytes_p():
    int128._from_bytes(_BYTES)
"""


print("Making cython request to get bytes implementation:")
print(timeit.timeit(stmt='to_bytes_c()', setup=setup, number=10000))
print("Making python request to get bytes implementation:")
print(timeit.timeit(stmt='to_bytes_p()', setup=setup, number=10000))
print("Making cython request to get int fro bytes implementation:")
print(timeit.timeit(stmt='from_bytes_c()', setup=setup, number=10000))
print("Making python request to get int fro bytes implementation:")
print(timeit.timeit(stmt='from_bytes_p()', setup=setup, number=10000))
