# pyception [![Build Status](https://travis-ci.org/jonathansp/pyception.svg?branch=master)](https://travis-ci.org/jonathansp/pyception) [![PyPI version](https://badge.fury.io/py/pyception.svg)](https://badge.fury.io/py/pyception) [![JSPDicas](https://img.shields.io/badge/jspdicas-approved-blue.svg)](https://mest.re)
A more meaningful exception's collection for Python.

Exceptions are important in Python. Throwing and handling it correctly avoid application stopping abruptly and make debug better.
- Simple and lightweight library.
- Collection inspired by frameworks and languages such as .NET, javasdk, ruby, php etc.

Feel free to open a pull request! (Please, use [Jeremy Mack's](http://seesparkbox.com/foundry/semantic_commit_messages) commit style.)

Simple usage:

```python

    from pyception.security import PrivilegeNotHeldException

    if not user.has_previlege('admin'):
        raise PrivilegeNotHeldException('Not allowed.')

        # instead of EnvironmentError or even Exception
```

Namespaces:

```python
import pyception.application
import pyception.configuration
import pyception.collection
import pyception.data
import pyception.io
import pyception.networking
import pyception.security
import pyception.system
import pyception.text
```
