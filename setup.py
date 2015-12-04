# -*- coding: utf-8 -*-

from pyception import __author__ as author
from pyception import __email__ as email
from pyception import __version__ as version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()


def load_from(file_name):
    with open(file_name) as requirements:
        return requirements.read().split('\n')

setup(
    name='pyception',
    version=version,
    description="A more meaningful exception's collection for Python",
    long_description=readme,
    author=author,
    author_email=email,
    url='https://github.com/jonathansp/pyception',
    packages=[
        'pyception',
    ],
    package_dir={
        'pyception': 'pyception'
    },
    include_package_data=True,
    install_requires=load_from("requirements.txt"),
    license="LGPLv3",
    zip_safe=False,
    keywords='exceptions',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=load_from("requirements_dev.txt")
)
