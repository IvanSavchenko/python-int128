#cython: boundscheck=False
#cython: wraparound=False
#cython: cdivision=True

"""Int 128 implementation for Python.

This module contains the implementation int128 for Python.
The main functionality is to encode to the binary format or any other as and
decode from bytes to integer.
"""

import struct


cdef extern from "extensions.h":
    # It is here just to let cython pass the first step, which is generating
    # the .c file.
    ctypedef unsigned long long int128
    ctypedef unsigned long long int64

# Constants
# Value in bytes for Int128.
cdef unsigned short INT128_BYTES = 16

# Value in bits for Int128.
cdef unsigned short INT128_BITS = 128

# Value in bytes for Int64.
cdef unsigned short INT64_BYTES = 8

# Value in bits for Int64.
cdef unsigned short INT64_BITS = 64

# Max int for Int64
cdef int64 INT64_MAX_VALUE = (1 << 64) - 1

# Struct formula for Int64.
cdef str INT64_STRUCT_FORMULA = 'Q'

# Bytes ordering patteron for struct module.
cdef dict BYTES_ORDERING = {
    'big': '>',
    'netword': '!',
    'little': '<',
    'native': '@'
}


cdef class Int128:
    """Int128 class."""
    cdef public int128 value

    def __init__(self, value=0):
        """Initialization."""
        self.value = value

    def to_bytes(self, value=None, byteorder='big'):
        """Get integer in binary format for Python 3."""
        if value is None:
            value = self.value

        return self._to_bytes(value, byteorder)

    cdef bytes _to_bytes(self, int128 value, str byteorder):
        """Cythonize the byte creation from integer."""
        cdef list separeted_ints, words
        cdef str formula = '!2Q'
        cdef int128 first_word, second_word

        # 2 integers will be converted as int64.
        first_word = value >> INT64_BITS
        second_word = value

        first_word = first_word & INT64_MAX_VALUE
        second_word = first_word & INT64_MAX_VALUE

        # Here this 2 integers will be concatenated.
        return struct.pack(formula, first_word, second_word)
