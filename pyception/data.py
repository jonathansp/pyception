# -*- encoding: utf-8 -*-

import sys

from pyception.wrapper import PyceptionModule

EXCEPTIONS = {
    'ConcurrencyException':       (ValueError, 'The exception that is thrown by the during an IO operation when the data is locked by other instance.'),
    'ConstraintException':        (ValueError, 'The exception that is thrown when attempting an action that violates a constraint.'),
    'DataException':              (ValueError, 'The exception that is thrown when a generic data error happens.'),
    'DataMisalignedException':    (ValueError, 'The exception that is thrown when a unit of data has an incorrect position, size or alignment.'),
    'DuplicateNameException':     (ValueError, 'The exception that is thrown when a duplicate object name is found.'),
    'EvaluateException':          (ValueError, 'The exception that is thrown when some data cannot be evaluated.'),
    'FieldAccessException':       (ValueError, 'The exception that is thrown when there is an invalid attempt to access private or invalid field.'),
    'InvalidDataException':       (ValueError, 'The exception that is thrown when a data stream is in an invalid format or value.'),
    'ReadOnlyException':          (ValueError, 'The exception that is thrown when you try to change the value of a read-only data.')
}

sys.modules[__name__] = PyceptionModule(__name__, EXCEPTIONS)
