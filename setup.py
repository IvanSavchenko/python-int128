#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Library setup."""

import re

from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('int128/__init__.py') as init_file:
    version = re.search('__version__ = \'(.*?)\'', init_file.read()).group(1)

with open('int128/requirements/requirements.txt') as req:
    requirements = req.readlines()

with open('int128/requirements/requirements_test.txt') as req_test:
    requirements_test = req_test.readlines()


setup(
    name='python-int128',
    version=version,
    description="Int128 implementation for Python",
    long_description=readme + '\n\n' + history,
    author="Ivan Savchenko",
    author_email='iam.savchenko@gmail.com',
    url='https://github.com/IvanSavchenko/python-int128',
    packages=[
        'int128',
    ],
    package_dir={'int128':
                 'int128'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords=[
        'int128',
        'python int128',
        'integer 128',
        'integer to bytes'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=requirements_test
)
