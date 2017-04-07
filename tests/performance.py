"""Example of using int128 module."""
from __future__ import absolute_import

import timeit


setup = """

import random
import int128


NUMBER = random.randint(1, ((1 << 128) - 1))

instance = int128.Int128()
"""


print("Making request to cython implementation:")
print(timeit.timeit(stmt='instance.to_bytes(NUMBER)', setup=setup, number=10000))
