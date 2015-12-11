# pyception [![Build Status](https://travis-ci.org/jonathansp/pyception.svg?branch=master)](https://travis-ci.org/jonathansp/pyception) [![PyPI version](https://badge.fury.io/py/pyception.svg)](https://badge.fury.io/py/pyception) [![JSPDicas](https://img.shields.io/badge/jspdicas-approved-blue.svg)](https://mest.re)

A more meaningful exception's collection for Python

* simple and lightweight library
* inspired on frameworks and languages such as .NET, javasdk, ruby, php etc.

Feel free to open a pull request! (Please, use [Jeremy Mack's](http://seesparkbox.com/foundry/semantic_commit_messages) commit style.)

Simple usage:

``` python

    import pyception

    if not user.has_previlege('admin'):
        raise pyception.security.PrivilegeNotHeldException('Not allowed.')

```

Namespaces:

``` python
import pyception.application
import pyception.configuration
import pyception.data
import pyception.io
import pyception.networking
import pyception.security
import pyception.system
import pyception.text
```
