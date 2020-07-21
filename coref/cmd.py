from coref import *
from coref.ns import nsGet, nsSet

def nsCmd(ns):
    argv = nsGet(ns, "/etc/argv", []).value
    root = nsGet(ns, "/config/cmd.path").value
    is_cmd_run = nsGet(ns, "/config/cmd.run")
    if is_cmd_run == TRUE:
        return ns
    for k in argv:
        out = ns.f("{}/{}".format(root, k))()
        nsSet(ns, "/config/cmd.run", True)
    return ns
