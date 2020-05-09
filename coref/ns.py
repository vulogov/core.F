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


def fNS(ns={}, **kw):
    ns = Namespace(**ns)
    ns += Namespace(**kw)
    return ns
