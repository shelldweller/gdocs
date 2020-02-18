from setuptools import setup, find_packages
import os.path
import re

with open('README.md') as f:
    readme = f.read()

with open(os.path.join(os.path.dirname(__file__), 'gdocs', 'VERSION')) as f:
    version = f.read().strip()

setup(
    name='gdocs',
    version=version,
    description='Library to access and parse Google Docs',
    long_description=readme,
    license='Public Domain',
    packages=find_packages(exclude=('tests')),
    package_data={
        'gdocs': ['VERSION']
    },
    install_requires = [],
    extras_require={
        'auth': [
            'google-api-python-client',
            'google-auth-httplib2',
            'google-auth-oauthlib',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: Public Domain',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing'
    ],
)
