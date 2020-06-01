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

def nsLn(ns, _from, _to):
    v = ns.V(_from)
    if nsNothing(v):
        return v
    return ns.V(_to, v)

def nsDir(ns, path):
    return ns.cd(path)

def nsLs(ns, path):
    return ns.ls(path)

def nsMkdir(ns, path):
    return ns.mkdir(path)

def nsMemory(ns):
    return sys.getsizeof(ns)
