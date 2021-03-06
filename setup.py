# -*- coding: utf-8 -*-
import setuptools


requirements = [
    'Flask',
    'Flask-WTF',
    'Flask-Login',
    'wtforms-components',
    'PyGithub'
]

test_requirements = ['flake8']

setuptools.setup(
    name="git-kloc",
    version="0.0.1",
    url="https://github.com/joeirimpan/git_kloc",

    author="Joe Paul",
    author_email="joeirimpan@gmail.com",

    description="A simple flask application to display"
    "how much a user contributed to an organisation",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=requirements,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
