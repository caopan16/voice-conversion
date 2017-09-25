#!/usr/bin/env python

from setuptools import setup, find_packages

import os
if os.path.exists('README.md'):
    README = open('README.md').read()
else:
    README = ""  # a placeholder, readme is generated on release
CHANGES = open('CHANGES.md').read()

setup(
    name="sprocket",
    version="0.2.4",
    description='sprocket: Voice Conversion Tool Kit',
    url='https://github.com/k2kobayashi/sprocket',
    author='Kazuhiro KOBAYASHI',
    author_email='root.4mac@gmail.com',
    packages=find_packages(),
    long_description=(README + '\n' + CHANGES),
    license='MIT',
    install_requires=open('requirements.txt').readlines(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
        'License :: OSI Approved :: MIT License',
    ]
)
