"""Int 128 implementation for Python on Python.

This module contains the implementation int128 for Python.
The main functionality is to encode to the binary format or any other as and
decode from bytes to integer.
"""

import struct

from . import constants


class Int128(object):
    """Int128 class."""

    TO_BYTES_PATTERN = "_to_bytes_python_{}"
    FROM_BYTES_PATTERN = "_from_bytes_python_{}"

    def __init__(self, value=None):
        """Initialization."""
        self.value = value

        self.to_bytes = \
            getattr(self, self.TO_BYTES_PATTERN.format(constants.PY_VERSION))

        self.from_bytes = \
            getattr(self, self.FROM_BYTES_PATTERN.format(constants.PY_VERSION))

    def _to_bytes_python_3(self, value=None, byteorder='big'):
        """Get integer in binary format for Python 3."""
        if value is None:
            value = self.value

        return value.to_bytes(constants.INT128_BYTES, byteorder=byteorder)

    def _to_bytes_python_2(self, value=None, byteorder='big'):
        """Get integer in binary format for Python 2.

        This functions will separate 128bit integer to several 64bit integers
        and then encode it to binary format and return a result of its
        concatenation.
        """
        if value is None:
            value = self.value

        # 2 integers will be converted as int64.
        first_word = ((value >> constants.INT64_BITS) &
                      constants.INT64_MAX_VALUE)
        second_word = value & constants.INT64_MAX_VALUE

        formula = '{ordering}{count}{pattern}'.format(
            ordering=constants.BYTES_ORDERING[byteorder],
            count=constants.INT128_BITS / constants.INT64_BITS,
            pattern=constants.INT64_STRUCT_FORMULA)

        # Here this 2 integers will be concatenated.
        return struct.pack(formula, first_word, second_word)

    def _from_bytes_python_3(self, int_in_bytes, byteorder='big'):
        """Get integer from bytes for Python 3."""
        return int.from_bytes(int_in_bytes, byteorder=byteorder)

    def _from_bytes_python_2(self, int_in_bytes, byteorder='big'):
        """Get integer from bytes for Python 2.

        This function will decode bytes as 128 bit integer separate on
        2 64 integer. The result will be the concatenation of 64 integers
        with respect to the order.
        """
        formula = '{ordering}{count}{pattern}'.format(
            ordering=constants.BYTES_ORDERING[byteorder],
            count=constants.INT128_BITS / constants.INT64_BITS,
            pattern=constants.INT64_STRUCT_FORMULA)

        # Get 2 words as int64.
        first_word, second_word = struct.unpack(formula, int_in_bytes)

        # Return the concatenation.
        first_word = first_word << constants.INT64_BITS
        return first_word | second_word
