from coref.internal.monad import *

def nsSet(ns, key, val):
    if nsGet(ns, "/config/var.redefine", True) is True:
        return ns.V(key, val)
    return NONE

def nsGet(ns, path, default=NONE):
    if path[-1] == '/':
        path = path[:-1]
    v = ns.V(path)
    if v is NONE or v is None or v is Nothing():
        if isinstance(default, Monad):
            return default
        return Just(default)
    return v
