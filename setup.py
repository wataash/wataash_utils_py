# SPDX-License-Identifier: Apache-2.0

# https://click.palletsprojects.com/en/7.x/setuptools/

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='wataash_utils',
    version='0.1.0',
    url='https://github.com/wsh/wataash_utils',
    author='Wataru Ashihara',
    author_email='wataash@wataash.com',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    license='Apache-2.0',
    description='wataash\'s personal utilities',
    long_description=long_description,
    keywords='wataash_utils',
    install_requires=[
        'logzero>=1.6.3',
    ],
    packages=find_packages(),
)
