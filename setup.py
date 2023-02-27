"""
    Ziti Edge Management

    OpenZiti Edge Management API  # noqa: E501

    The version of the OpenAPI document: 0.25.6
    Contact: help@openziti.org
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "openziti-edge-management"
VERSION = "0.25.6"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Ziti Edge Management",
    author="OpenZiti",
    author_email="help@openziti.org",
    url="https://github.com/openziti-test-kitchen/openziti-edge-management-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Ziti Edge Management"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    OpenZiti Edge Management API  # noqa: E501
    """
)
