from coref import *
import fnmatch
from hy import read_str, eval

def nsImportPfun(ns, env, *vpath):
    for p in vpath:
        env.update(nsLs(ns, p).value)
    return env


def nsHYmkenv(ns, **kw):
    env = globals()
    env["nsGet"] = nsGet
    env["nsSet"] = nsSet
    env["f"] = nsGet(ns, "/bin/f")
    env["F"] = nsGet(ns, "/bin/F")
    env["stamp"] = nsGet(ns, "/bin/stamp")
    env["ns"] = ns
    return env
