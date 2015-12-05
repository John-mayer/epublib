# -*- coding: utf-8 -*-
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('click/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='epublib',
    version=version,
    description='Library for writing and reading epub',
    long_description='Library for writing and reading epub',
    url='https://github.com/takuan-osho/epublib',
    author='SHIMIZU Taku',
    author_email='shimizu.taku@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],
    keywords='epub library',
    packages=find_packages(exclude=['docs', 'tests', '*.egg-ingo'])
)
