#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='snapchat-yt',
    version='1.0.0',
    description='Send youtube clips through Snapchat',
    long_description=open('README.md').read(),
    author='Charles C. Lee',
    author_email='charleschanlee@gmail.com',
    url='https://github.com/ChanChar/snapchat-yt',
    install_requires=[
        'pysnap>=0.1.1'
    ],
    dependency_links = ['https://github.com/martinp/pysnap/tarball/master#egg=pysnap-0.1.1'],
    license=open('LICENSE').read()
)