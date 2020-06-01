import sys
from coref import *

def nsSet(ns, key, val):
    if nsGet(ns, "/config/var.redefine", True) == TRUE:
        return ns.V(key, val)
    return NONE

def nsGet(ns, path, default=NONE):
    if path[-1] == '/':
        path = path[:-1]
    v = ns.V(path)
    if v == NONE or v == Nothing() or v is None:
        if isinstance(default, Monad):
            return default
        return Just(default)
    return v
