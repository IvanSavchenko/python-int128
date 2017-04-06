"""Compile cython files."""
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Python Int128',
    ext_modules=cythonize("int128/int128.pyx"),
)
