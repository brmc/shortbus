#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pyyaml',
    'lxml'
]

test_requirements = []

setup(
    name='shortbus',
    version='0.2.0',
    description="Tools to convert Sublime Text snippets into Jetbrains live templates and vice versa",
    long_description=readme + '\n\n' + history,
    author="Brian McClure",
    author_email='brian@mcclure.pw',
    url='https://github.com/brmc/shortbus',
    packages=[
        'shortbus',
    ],
    package_dir={'shortbus':
                 'shortbus'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='shortbus',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
