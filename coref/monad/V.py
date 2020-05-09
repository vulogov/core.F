from .Value import Value
from .Dict import Dict
from .Set import Set
from .L import L
from pymonad.Monad import *

def v(*values, **kw):
    if not values and not kw:
        return Nothing
    if values and len(values) == 1:
        if isinstance(values[0], list) is True:
            return L(*values[0])
        elif isinstance(values[0], dict) is True:
            return Dict(**values[0])
        elif isinstance(values[0], set) is True:
            return Set(*values[0])
        else:
            return Value(values[0])
    if values and len(values) > 1:
        return L(*values)
    if kw:
        return Dict(**kw)
    return Nothing
