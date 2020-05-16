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
from coref.internal import *
from pymonad import curry
from functools import partial


def fV(ns, path):
    try:
        return dpget(ns, path)
    except KeyError:
        return None

def V(ns, path, value=None):
    if value is None:
        return v(fV(ns, path))
    return fSet(ns, path, value)

def fMk(ns, path, data):
    res = V(ns, path)
    if res == NONE:
        dpnew(ns, path, data)
    else:
        if isinstance(res, dict) is True and isinstance(data, dict) is True:
            dpget(ns, path).update(data)
        else:
            dpset(ns, path, data)
    return ns


def fMkdir(ns, path):
    from coref.internal.path import expandPath

    dir = NONE
    res = V(ns, path)
    if res is NONE:
        for _p in expandPath(path):
            try:
                dpget(ns, _p)
            except KeyError:
                dpnew(ns, _p, {
                    '__name__'  : _p,
                    '__stamp__' : time.time(),
                    '__id__' : str(uuid.uuid4()),
                    '__dir__' : True
                })
        dir = Namespace(
            __name__ = path,
            __stamp__ = time.time(),
            __id__ = str(uuid.uuid4()),
            __dir__ = True
        )
        dpnew(ns, path, dir.getValue())
    else:
        return [Namespace(res)]
    return [dir]

def fCd(ns, path):
    res = V(ns, path)
    if res is NONE:
        return [NONE]
    if res.get('__dir__', False):
        return [NONE]
    return  [Namespace(res)]


def fGet(ns, path):
    res = V(ns, path)
    return [res]

def fSet(ns, path, value):
    _base = os.path.dirname(path)
    fMkdir(ns, _base)
    res = V(ns, path)
    if res == NONE:
        dpnew(ns, path, value)
    else:
        dpset(ns, path, value)
    return [value]

def f(ns, name):
    def _nullfun(*args, **kw):
        return None
    print("f()", name)
    try:
        res = dpget(ns.getValue(), name)
        print("=====",res)
    except KeyError:
        return _nullfun
    return res

def I(ns, path, fun):
    _fun = partial(fun, ns)
    fSet(ns, path, _fun)
    return [_fun]

def fNS(ns={}, **kw):
    ns = Namespace(**ns)
    ns += Values (
        __name__ = "/",
        __stamp__ = time.time(),
        __id__ = str(uuid.uuid4()),
        __dir__ = True
    )
    ns += Namespace(**kw)
    return (curry(f)(ns), ns)
