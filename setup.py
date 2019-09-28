#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="pypixel",
    version="1.0.0",
    author="Jiacheng Huang",
    author_email="Dylan.JiaCheng.Huang@outlook.com",
    description="A Image Processing Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/JiaCheng-Huang/pypixel",
    packages=find_packages(),
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)

