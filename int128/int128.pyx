#cython: boundscheck=False
#cython: wraparound=False

"""Int 128 implementation for Python on Cython.

This module contains the implementation int128 for Python on Cython.
The main functionality is to encode 128 bit integers to the binary format
and decode from bytes to integer.
"""

import _struct


cdef extern from "extensions.h":
    # Extend our types with int128 and int64 from C.
    ctypedef unsigned long long int128
    ctypedef unsigned long long int64

# Constants
# Value in bytes for Int64.
cdef unsigned short INT64_BYTES = 8

# Value in bits for Int64.
cdef unsigned short INT64_BITS = 64

# Max int for Int64
cdef int64 INT64_MAX_VALUE = (1 << 64) - 1

# Bytes ordering list and patterns for struct module.
cdef tuple BYTES_ORDERS = ('big', 'network', 'little', 'native')
cdef dict BYTES_ORDERING = {
    'big': '>',
    'network': '!',
    'little': '<',
    'native': '@'
}


cdef class Int128:
    """Int128 class.

    Class which implements main functionality for encode and decode 128 bit
    integers to or from binary view.

    Example of usage:
        some_128bit_int = ...
        int128_coder = Int128()

        int128_in_bytes = int128_coder.to_bytes(some128_bit_int)
        some_128bit_int = int128_coder.from_bytes(int128_in_bytes)

    Class methods support bytes encoding types, so you can specify which
    exctly one you want ('big', 'little', 'network', 'native')
    """

    # Public access.
    cdef public int128 value

    def __cinit__(self, int128 value=0):
        """Initialization.

        :param int128 value: integer to be initialized with class instance.
        """
        self.value = value

    cpdef bytes to_bytes(self, int128 value, str byteorder='big'):
        """Encode integer to bytes.

        This method perform encoding integer to bytes and returning it.

        This method will separate 128 bit integer for 2 64 integer with
        using of bit shifting and after will just encode both of them
        as 64 bit integers.

        :param int128 value: integer which will be encoded to bytes.
        :param str byteorder: one of the byteorders which set up in which
            byte order response will be. Must be one of the next:
            'big', 'little', 'native', 'network'.

        :return: 16 bytes which represents the provided integer
        :return type: bytes
        """
        if value is None:
            value = self.value

        # Need to rework it!
        if byteorder not in BYTES_ORDERS:
            raise TypeError('Bad byte order provided. Need to be one of this:',
                            BYTES_ORDERS)

        cdef int64 first_word, second_word

        # 2 integers will be converted as int64.
        first_word = (value >> INT64_BITS)
        second_word = value

        first_word = first_word & INT64_MAX_VALUE
        second_word = second_word & INT64_MAX_VALUE

        return _struct.pack('%s2Q' % BYTES_ORDERING[byteorder],
                            first_word, second_word)

    cpdef int128 from_bytes(self, bytes value, str byteorder='big'):
        """Decode integer to bytes.

        This method perform decoding integer from bytes and returning it.

        This method will decode bytes as 128 bit integer separated on
        2 64 integer. The result will be the concatenation of 64 integers
        with respect to the order.

        :param bytes value: bytes, maximum 16, from which int128 will be
            decoded.
        :param str byteorder: one of the byteorders which set up in which
            byte order response will be. Must be one of the next:
            'big', 'little', 'native', 'network'.

        :return: decoded integer
        :return type: int128
        """
        cdef int128 first_word
        cdef int64 second_word

        # Get 2 words as int64.
        first_word, second_word = \
            _struct.unpack('%s2Q' % BYTES_ORDERING[byteorder], value)

        first_word = first_word << INT64_BITS
        return first_word | second_word
