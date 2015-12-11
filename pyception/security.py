# -*- encoding: utf-8 -*-

import sys

from pyception.wrapper import PyceptionModule

EXCEPTIONS = {
    'AuthenticationException':     (Exception, 'The exception that is thrown when authentication fails.'),
    'CryptographicException':      (Exception, 'The exception that is thrown when an error occurs during a cryptographic operation.'),
    'HostProtectionException':     (Exception, 'The exception that is thrown when a denied host resource is detected.'),
    'InvalidCredentialException':  (Exception, 'The exception that is thrown when authentication fails.'),
    'MemberAccessException':       (Exception, 'The exception that is thrown when an invalid attempt to access a role or resource happens.'),
    'SecurityException':           (Exception, 'The exception that is thrown when a security error is detected.'),
    'VerificationException':       (Exception, 'The exception that is thrown when the security policy blocks an access.'),
    'PrivilegeNotHeldException':   (Exception, 'The exception that is thrown when some user needs a privilege that does not have.'),
    'PolicyException':             (Exception, 'The exception that is thrown when policy forbids some operation.'),
    'UnauthorizedAccessException': (Exception, 'The exception that is thrown when the system denies an access to some resource or operation.')
}

sys.modules[__name__] = PyceptionModule(__name__, EXCEPTIONS)
