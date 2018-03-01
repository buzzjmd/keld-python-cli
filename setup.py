# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

setup_requirements = [
    'setuptools_scm',
]

requirements = [
    'Click>=6.0',
]

console_script_entry_points = [
    'keld=keldcli:cli'
]

setup(
    name='keldcli',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    use_scm_version=True,
    setup_requires=setup_requirements,
    install_requires=requirements,
    entry_points={
        'console_scripts': console_script_entry_points
    },
)
