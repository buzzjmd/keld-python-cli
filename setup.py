# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='keldcli',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    entry_points={
        'console_scripts': [
            'keld=keldcli:cli'
        ]
    },
)
