#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='oscp',
    author='Marc Gurreri',
    version='1.0',
    author_email='me@me.com',
    description='OSCP transforms for Maltego',
    license='GPLv3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    package_data={
        '': ['*.gif', '*.png', '*.conf', '*.mtz', '*.machine']  # list of resources
    },
    install_requires=[
        'canari==1.1',
        'lxml',
        'python-libnmap',
        'python-nmap',
        'pyiptools'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
