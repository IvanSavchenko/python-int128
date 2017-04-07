"""Example of using int128 module."""
from __future__ import absolute_import

import timeit


setup = """

import random
import int128


NUMBER = random.randint(1, ((1 << 128) - 1))

instance_cython = int128.Int128()
instance_python = int128._Int128()

def to_bytes(instance):
    instance.to_bytes(NUMBER)
"""


print("Making request to cython implementation:")
print(timeit.timeit(stmt='to_bytes(instance_cython)', setup=setup, number=10000))
print("Making request to python implementation:")
print(timeit.timeit(stmt='to_bytes(instance_python)', setup=setup, number=10000))
