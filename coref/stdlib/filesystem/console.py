import sys
import time
from coref import *
from coref.mod import nsValues, nsList
from coref.internal.rb import RingBuffer
from collections import namedtuple
from Cheetah.Template import Template

_CONSOLE = namedtuple('Console', ['stamp', 'msg'])

def nsConsole(ns, *args, **kw):
    print("HHH",ns)
    if ns.V("/isConsole") == FALSE:
        return False
    _msg = ""
    for a in args:
        if isinstance(s, str) is True:
            t = str(Template(a, searchList=[kw]))
            _msg += t
    _cons = _CONSOLE(stamp=time.time(), msg=_msg)
    if ns.V("/nsDirect") == TRUE:
        if ns.V("/nsStdout") == TRUE:
            with indent(4, quote=colored.green(' : ')):
                puts(_cons.msg)
        else:
            ns.V("/fd").value.write(_cons.msg+"\n")
    else:
        ns.V("/buffer").value.append(_cons)
    return True

def nsConsoleStop(ns):
    if ns.V("/etc/flags/stdout") == FALSE:
        ns.V("/etc/console/fd").value.close()
    return True

def nsConsoleInit(ns):
    ns.V("/dev/console/a", True)
    ns.V("/dev/console/isConsole", ns.V("/etc/flags/console").value)
    ns.V("/dev/console/isStdout", ns.V("/etc/flags/stdout"))
    ns.V("/dev/console/isDirect", ns.V("/etc/flags/direct"))
    if ns.V("/etc/flags/stdout") == TRUE:
        ns.V("/dev/console/fd", sys.stdout)
    else:
        _path = "{}/console.out".format(ns.V('/sys/env/apphome').value)
        ns.V("/dev/console/fd", open(_path, 'w'))
    ns.V("/dev/console/buffer", RingBuffer(capacity=nsGet(ns, "/etc/consoleSize", 100).value, dtype=_CONSOLE))
    return True

_ctx = {
    '/dev/console': {
        'send': nsConsole,
    }
}

_mkdir = [
    '/dev/console',
]

_init = {
    998: {
        'console': {
            'start': nsConsoleInit,
            'stop': nsConsoleStop,
        }
    }
}
