import atexit
from coref import *

def nsInit(ns):
    atexit.register(nsStop, ns)
    init = ns.dir("/etc/init.d")
    for i in init.sort():
        ctx = ns.dir(f"/etc/init.d/{i}")
        for k in ctx.sort():
            start_fun = ns.V(f"/etc/init.d/{i}/{k}/start")
            if isNothing(start_fun) is True:
                continue
            if start_fun.value() is not True:
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
            if stop_fun.value() is not True:
                break
    return
