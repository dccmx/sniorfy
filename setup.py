#!/usr/bin/env python
from setuptools import setup

version = "0.2.0"

setup(
    name="sniorfy",
    version=version,
    packages=["sniorfy", "sniorfy.ioloop"],
    package_data={
        "sniorfy": ["README.md"],
        },
    author="dccmx",
    author_email="dccmx@dccmx.com",
    url="http://www.simpletp.org/sniorfy",
    download_url="https://github.com/dccmx/sniorfy/tarball/%s" % version,
    license="MIT",
    description="sniorfy is an open source rpc framework in python",
)
