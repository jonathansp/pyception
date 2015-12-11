# -*- encoding: utf-8 -*-

import sys

from pyception.wrapper import PyceptionModule

EXCEPTIONS = {
    'AccessViolationException':      (SystemError, 'The exception that is thrown when data is read from or written to somewhere without explicit access.'),
    'ContextMarshalException':       (SystemError, 'The exception that is thrown when an attempt to marshal an object across a context boundary fails.'),
    'InsufficientMemoryException':   (SystemError, 'The exception that is thrown when there is not available memory to handle some data.'),
    'PlatformNotSupportedException': (SystemError, 'The exception that is thrown when a feature does not run on a particular platform.')
}

sys.modules[__name__] = PyceptionModule(__name__, EXCEPTIONS)
