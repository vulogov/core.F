import atexit
from coref import *

def nsInitRun(ns, path, name, action=None):
    _fun = ns.V(f"{path}/{name}")
    if isNothing(_fun) is True:
        return False
    print ("init()", f"{path}/{name}")
    if action is None:
        if callable(_fun.value) is not True:
            return False
        if _fun.value() is not True:
            return False
    else:
        return action(ns, _fun)
    return True

def nsInit(ns):
    atexit.register(nsStop, ns)
    init = ns.dir("/etc/init.d")
    for i in init.sort():
        ctx = ns.dir(f"/etc/init.d/{i}")
        for k in ctx.sort():
            path = f"/etc/init.d/{i}/{k}"
            if nsInitRun(ns, path, 'start') is False:
                break
    return

def nsStop(ns):
    init = ns.dir("/etc/init.d")
    for i in init.sort().reverse():
        ctx = ns.dir(f"/etc/init.d/{i}")
        for k in ctx.sort().reverse():
            stop_fun = ns.V(f"/etc/init.d/{i}/{k}/stop")
            if isNothing(stop_fun) is True:
                continue
            if callable(stop_fun) is not True:
                continue
            if stop_fun.value() is not True:
                break
    return
