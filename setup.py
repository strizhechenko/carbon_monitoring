#!/usr/bin/env python

'''The setup and build script for the carobn_monitoring.'''

import os

from setuptools import setup, find_packages
from pip.req import parse_requirements as parse_reqs


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


INSTALL_REQS = [str(ir.req) for ir in parse_reqs('requirements.txt', session=1)]

setup(
    name='carbon_monitoring',
    version='0.0.2',
    author='Oleg Strizhechenko',
    author_email='oleg.strizhechenko@gmail.com',
    license='GPL',
    url='https://github.com/strizhechenko/carbon_monitoring',
    keywords='monitoring influxdb alerter',
    description='all was so bad, so I going invent a wheel',
    long_description=(read('README.md')),
    packages=find_packages(exclude=['tests*']),
    install_requires=INSTALL_REQS,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
)
