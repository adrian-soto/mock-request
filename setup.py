#!/usr/bin/env python

import re
import ast
from os import path
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

PACKAGE_NAME = 'mock_request'
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'README.md'), encoding='utf-8') as fp:
    README = fp.read()
with open(path.join(HERE, PACKAGE_NAME, '__init__.py'), 'rb') as fp:
    VERSION = str(ast.literal_eval(_version_re.search(
fp.read().decode('utf-8')).group(1)))

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    packages=[PACKAGE_NAME],
    install_requires=["pandas", "requests"],
    description="mock API requests using pickled request objects",
    long_description=README,
    long_description_content_type='text/markdown',
    author='Adrián Soto',
    maintainer='Adrián Soto',
    url='https://github.com/adrian-soto/mock-request',
    classifiers=["Programming Language :: Python :: 3"]
)
