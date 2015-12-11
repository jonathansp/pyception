# -*- encoding: utf-8 -*-

import sys

from pyception.wrapper import PyceptionModule

EXCEPTIONS = {
    'ConfigurationException': (ValueError, 'This exception is thrown when there is a configuration issue.')
}

sys.modules[__name__] = PyceptionModule(__name__, EXCEPTIONS)
