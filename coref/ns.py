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


def V(ns, path):
    try:
        res = dpget(ns, path)
    except KeyError:
        return NONE
    return v(res)

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
    dir = NONE
    res = V(ns, path)
    if res is NONE:
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


def fNS(ns={}, **kw):
    ns = Namespace(**ns)
    ns += Values (
        __name__ = "/",
        __stamp__ = time.time(),
        __id__ = str(uuid.uuid4()),
        __dir__ = True
    )
    ns += Namespace(**kw)
    return ns
