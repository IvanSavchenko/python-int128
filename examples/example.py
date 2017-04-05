"""Example of using int128 module."""

from __future__ import absolute_import

import random

import int128

NUMBER = random.randint(1, ((1 << 128) - 1))


if __name__ == '__main__':
    # instance = int128.Int128(NUMBER)
    instance = int128.Int128()

    # binary_int = instance.to_bytes()
    binary_int = instance.to_bytes(NUMBER)

    int_from_bytes = instance.from_bytes(binary_int)

    print(binary_int, int_from_bytes)
