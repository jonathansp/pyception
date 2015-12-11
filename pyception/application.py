# -*- encoding: utf-8 -*-

import sys

from pyception.wrapper import PyceptionModule

EXCEPTIONS = {
    'ApplicationException':            (SystemError, 'The exception that is thrown when there is an generic application error.'),
    'AppDomainUnloadedException':      (SystemError, 'The exception that is thrown when an attempt is made to access an unloaded application.'),
    'ArgumentOutOfRangeException':     (SystemError, 'The exception that is thrown when the value or argument is outside from allowed range.'),
    'CannotUnloadAppDomainException':  (SystemError, 'The exception that is thrown when an attempt to unload an application fails.'),
    'EntryPointNotFoundException':     (SystemError, 'The exception that is thrown when an attempt to load a class, plugin or module fails due to the absence of an method.'),
    'InvalidCastException':            (SystemError, 'The exception that is thrown for invalid casting or explicit conversion.'),
    'InvalidOperationException':       (SystemError, 'The exception that is thrown when a method call is invalid for the object’s current state.'),
    'InvalidLibraryException':         (SystemError, 'The exception that is thrown when a library contains some invalid data.'),
    'MethodAccessException':           (SystemError, 'The exception that is thrown when there is an invalid attempt to access a private or protected method inside a class.'),
    'MissingMethodException':          (SystemError, 'The exception that is thrown when there is an attempt to access a method that does not exist.'),
    'OperationAbortedException':       (SystemError, 'This exception is thrown when an operation is aborted.')
}

sys.modules[__name__] = PyceptionModule(__name__, EXCEPTIONS)
