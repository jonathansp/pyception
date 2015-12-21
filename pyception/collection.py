# -*- encoding: utf-8 -*-

import sys

from pyception.wrapper import PyceptionModule

EXCEPTIONS = {
    'RangeError': (ValueError, 'Raised when a given numerical value, index or collection is out of range.')
}

sys.modules[__name__] = PyceptionModule(__name__, EXCEPTIONS)
