#!/usr/bin/env python
from setuptools import setup

version = '0.3.0'

setup(
    name='sniorfy',
    version=version,
    packages=['sniorfy'],
    package_data={
        'sniorfy': ['README.md'],
    },
    install_requires=['tornado'],
    author='dccmx',
    author_email='dccmx@dccmx.com',
    url='http://www.simpletp.org/sniorfy',
    download_url='https://github.com/dccmx/sniorfy/tarball/%s' % version,
    license='MIT',
    description='sniorfy is an open source rpc framework in python',
)
