"""Constants."""

import sys

# Version of python which is using.
PY_VERSION = sys.version_info.major

# Value in bytes for Int128.
INT128_BYTES = 16

# Value in bits for Int128.
INT128_BITS = 128

# Max value for Int128 (2 ** 128).
INT128_MAX_VALUe = (1 << INT128_BITS) - 1

# Value in bits for Int64.
INT64_BITS = 64

# Max int for Int64.
INT64_MAX_VALUE = (1 << INT64_BITS) - 1

# Struct formula for Int64.
INT64_STRUCT_FORMULA = 'Q'

# Bytes ordering patteron for struct module.
BYTES_ORDERING = {
    'big': '>',
    'netword': '!',
    'little': '<',
    'native': '@'
}
