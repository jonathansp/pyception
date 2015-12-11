# -*- encoding: utf-8 -*-

import sys

from pyception.wrapper import PyceptionModule

EXCEPTIONS = {
    'BroadcastNotSupportedException':   (Exception, 'The exception that is thrown when there is an attempt to broadcast an unbroadcastable data.'),
    'MulticastNotSupportedException':   (Exception, 'The exception that is thrown when there is an attempt to multicast an no multicastable data.'),
    'HttpException':                    (Exception, 'Represents an exception that occurred during the processing of HTTP requests.'),
    'ProtocolViolationException':       (Exception, 'The exception that is thrown when an error is made while using a network protocol.'),
    'SmtpException':                    (Exception, 'Represents the exception that is thrown when the is not able to complete a or operation.'),
    'SocketException':                  (Exception, 'The exception that is thrown when a socket error occurs.'),
    'PingException':                    (Exception, 'The exception that is thrown when cannot ping a host or server.'),
    'WebException':                     (Exception, 'The exception that is thrown when an error occurs while accessing the network through a pluggable protocol.')
}

sys.modules[__name__] = PyceptionModule(__name__, EXCEPTIONS)
