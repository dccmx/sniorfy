#!/usr/bin/env python
import distutils.core

kwargs = {}

version = "0.1.0"

distutils.core.setup(
    name="sniorfy",
    version=version,
    packages=["sniorfy"],
    package_data={
        "sniorfy": ["README.md"],
        },
    author="dccmx",
    author_email="dccmx@dccmx.com",
    url="http://www.simpletp.org/sniorfy",
    download_url="https://github.com/dccmx/sniorfy/tarball/%s" % version,
    license="MIT",
    description="sniorfy is an open source rpc framework in python",
    **kwargs
)
