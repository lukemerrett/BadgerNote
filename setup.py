__author__ = 'Luke Merrett'

from setuptools import setup, find_packages

setup(
    name="BadgerNote",
    packages=find_packages(),
    install_requires=['peewee', 'argparse'],
    author="Luke Merrett",
    author_email="lukeamerrett@gmail.com",
    url='https://github.com/lukemerrett/BadgerNote',
    license="GPL",
)
