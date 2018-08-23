from .Interface import Interface
from .Enumeration import Enumeration
from .Structure import Structure
from .Agent import Agent
from .TypeInfo import TypeInfo
from .Time import Time
from .Utils import Utils
from .ValueObject import ValueObject

#
# exceptions
#

class HttpException(Exception):
    pass

class JsonRpcSyntaxException(Exception):
    pass

class JsonRpcErrorException(Exception):
    pass

class DecodeException(Exception):
    pass
