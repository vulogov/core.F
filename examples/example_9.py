import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *

def appconfig(ns):
    print("Application config")

def cb(ns, path, _socket, _addr):
    c = 0
    while len(ns.V(f"{path}/in").value) > 0:
        data = ns.V(f"{path}/in").value.get()
        ns.V(f"{path}/out").value.put(data)
        c += 1
    if c > 0:
        return True
    return False


ns, f, F = NS()
F("/bin/initAppRegister", appconfig, level=1, action='start')
print("60000")
F("/bin/tcpServer", "0.0.0.0", 61000, cb)
print("60001")
F("/bin/tcpServer", "0.0.0.0", 61001, cb)
print("/bin/main")
F("/bin/main")

F("/usr/local/bin/daemon")
