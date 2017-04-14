"""Package initialization.

This packages contains of 2 instances, which implements inside all logic
for packing and unpacking 128 bit integers: one implemented on Cython,
another one CPython.

To be clear, there is no exactly need to use Python implementation, as
Cython's implementation works faster (sometimes 2x faster), but I've decided
to put it here and give access to it as _*function_name* because I can.

About performance: I don't know really why, but Cython and CPython
implementation have strange performance, sometimes even CPython works faster
that Cython, sometimes not. But, anyway, Cython performs better results what
it is on the hill so I would suggest you to use it as default.

So, what you can do:
    import int128

    int_b = int128.to_bytes(some_int)  # Cython implementation
    int_b = int128._to_bytes(some_int)  # Python implementation

    some_int = int128.from_bytes(int_b)  # Cython implementation
    some_int = int128._from_bytes(int_b)  # Python implementation
"""

from __future__ import absolute_import

__author__ = """Ivan Savchenko"""
__email__ = 'iam.savchenko@gmail.com'
__version__ = '0.2.0'

__all__ = ('to_bytes', 'from_bytes', '_to_bytes', '_from_bytes')

from int128.int128 import to_bytes
from int128.int128 import from_bytes

from int128.python.int128 import to_bytes as _to_bytes
from int128.python.int128 import from_bytes as _from_bytes
