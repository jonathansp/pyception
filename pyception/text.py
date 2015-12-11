# -*- encoding: utf-8 -*-

import sys

from pyception.wrapper import PyceptionModule

EXCEPTIONS = {
    'DecoderException':   (ValueError, 'The exception that is thrown when a decoder operation fails.'),
    'EncoderException':   (ValueError, 'The exception that is thrown when an encoder operation fails.'),
    'FormatException':    (ValueError, 'The exception that is thrown when the format of an argument does not meet with specifications.')
}

sys.modules[__name__] = PyceptionModule(__name__, EXCEPTIONS)
