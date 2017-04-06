#cython: language_level=3
#cython: boundscheck=False
#cython: wraparound=False

"""Int 128 implementation for Python.

This module contains the implementation int128 for Python.
The main functionality is to encode to the binary format or any other as and
decode from bytes to integer.
"""

# Constants
# Value in bytes for Int128.
cdef short INT128_BYTES = 16

# Value in bits for Int128.
cdef short INT128_BITS = 128

# Max value for Int128.
cdef long long INT128_MAX_VALUE = (1 << INT128_BITS) - 1

# Value in bits for Int64.
cdef short INT64_BITS = 64

# Max int for Int64
cdef long int INT64_MAX_VALUE = (1 << INT64_BITS) - 1

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
    cdef public long long value

    def __init__(self, value=0):
        """Initialization."""
        self.value = value

    def to_bytes(self, value=None, byteorder='big'):
        """Get integer in binary format for Python 3."""
        if value is None:
            value = self.value

        return self._to_bytes(value, byteorder)

    cdef long _to_bytes(self, long long value, str byteorder):
        cdef long long temp_result

        temp_result = value & INT64_MAX_VALUE

        return temp_result
