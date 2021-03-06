#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pyserial>=3.4', 'pynmea2>=1.15.0', 'haversine>=2.3.0', 'gps_api>=0.1.6']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Jialong Weng, Veronique Reagon",
    author_email='wngjia001@myuct.ac.za, rgnver001@myuct.ac.za',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Demonstrator for gps_api",
    entry_points={
        'console_scripts': [
            'gps_demo=gps_demo.cli:main',
        ],
    },
    install_requires=requirements
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='gps_demo',
    name='gps_demo',
    packages=find_packages(include=['gps_demo', 'gps_demo.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jialong-w/gps_demo',
    version='0.1.0',
    zip_safe=False,
)
