import io
import os
import re

from setuptools import find_packages, setup


with io.open("__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


def desc():
    return read("README.rst")


setup(
    name="Inheritance-Test",
    version=version,  
    url="https://github.com/valhuber/inheritance",
    license="BSD",
    author="Val Huber",
    author_email="valjhuber@gmail.com",
    description=(
        "Test inheritance (in same pkg) on PyPi."
    ),
    long_description=desc(),
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    entry_points={
        "console_scripts": ["inheritance-run=inheritance.run:start"]
    },
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=[
    ],
    extras_require={"jmespath": ["jmespath>=0.9.5"]},
    tests_require=["nose>=1.0", "mockldap>=0.3.0"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires="~=3.6"
)