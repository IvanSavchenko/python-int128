"""Compile cython files."""
from distutils.core import setup, Extension

setup(
    name='Python Int128',
    ext_modules=[Extension('int128.int128',
                           ['int128/int128.c'],
                           extra_compile_args=['-O2'])]
)
