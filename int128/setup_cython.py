"""Compile cython files."""
from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension(name='int128', sources=['int128.pyx'])
setup(ext_modules=cythonize(ext))
