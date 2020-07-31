import sys
import os
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *

def appconfig(ns):
    print("Application config")

def cb(ns, data):
    print("DATA:", data)
    return data

def push(ns):
    q = ns.V("/dev/pipe/emitter/test/out").value
    c = 0
    while True:
        q.put(bytes(f"{c}", "utf-8"))
        c += 1
        time.sleep(1)


ns, f, F = NS()
F("/bin/initAppRegister", appconfig, level=1, action='start')
F("/bin/pipeEmitter", "test", "tcp://*:61000", cb)
F("/bin/spawn", "pusher", push)
F("/bin/main")
F("/usr/local/bin/daemon")
