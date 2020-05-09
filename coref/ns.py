##
##
##

import time
import uuid
import os.path
from dpath.util import new as dpnew
from dpath.util import get as dpget
from dpath.util import set as dpset
from dpath.util import delete as dpdel
from coref.monad import *
from pymonad import curry

def expandPath(x):
    import os.path
    p = os.path.normpath(x)
    _p = p.split("/")
    _p = [i for i in _p if i]
    out = []
    for e in reversed(range(len(_p))):
        _d = "/"+"/".join(_p[:(e+1)])
        out.append(_d)
    return out

def unique(x):
    print(x)
    print(list(set(x)))
    return list(set(x))

def V(ns, path):
    try:
        res = dpget(ns, path)
    except KeyError:
        return NONE
    return v(res)


def fNS(ns={}, **kw):
    ns = Namespace(**ns)
    ns += Namespace(**kw)
    return ns
