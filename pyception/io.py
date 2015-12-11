# -*- encoding: utf-8 -*-

import sys

from pyception.wrapper import PyceptionModule

EXCEPTIONS = {
    'DriveNotFoundException':  (IOError, 'The exception that is thrown when trying to access a drive or NFS that is not available.'),
    'EndOfStreamException':    (IOError, 'The exception that is thrown when reading is attempted past the end of a stream.'),
    'FileLoadException':       (IOError, 'The exception that is thrown when a file cannot be loaded.'),
    'StorageException':        (IOError, 'The exception that is thrown when a storage operation fails.'),
    'PathTooLongException':    (IOError, 'The exception that is thrown when a pathname or filename is longer than the system-defined maximum length.'),
    'TimeoutException':        (IOError, 'The exception that is thrown when the time allotted for a process or operation has expired.')
}

sys.modules[__name__] = PyceptionModule(__name__, EXCEPTIONS)
