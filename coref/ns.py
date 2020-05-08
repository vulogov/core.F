##
##
##

import time
import uuid
import os.path
from pymonad import *
from dpath.util import new as dpnew
from dpath.util import get as dpget
from dpath.util import set as dpset
from dpath.util import delete as dpdel

def V(ns, path):
    if path == "/":
        return Just(ns)
    try:
        res = dpget(ns, path)
    except KeyError:
        return Nothing
    if isinstance(res, list):
        return List(res)
    return Just(res)

def fMkDirData():
    return {
        '__dir__': True,
        '__stamp__': time.time(),
        '__id__': str(uuid.uuid4())
    }

def fMk(ns, path, data):
    if path == "/":
        return Nothing
    if V(ns, path) != Nothing:
        return Nothing
    base = os.basename(path)
    fMk(ns, base, fMkDirData())
    return dpnew(ns, path, data)


def fNS(ns={}, **kw):
    ns = ns
    ns.update(fMkDirData())
    ns.update(kw)
    return curry(V)(ns)
