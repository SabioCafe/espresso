"""Módulo Setup."""
from setuptools import setup, find_packages

setup(
    name='espresso',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'espresso=app:cli',
        ],
    },
)