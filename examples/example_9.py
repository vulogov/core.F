import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *

def appconfig(ns):
    print("Application config")

def cb(*args):
    for i in args:
        print(type(i))
    print(args[1])
    return False


ns, f, F = NS()
F("/bin/initAppRegister", appconfig, level=1, action='start')
F("/bin/tcpServer", "127.0.0.1", 60000, cb)
F("/bin/tcpServer", "127.0.0.1", 60001, cb)
F("/bin/main")

F("/usr/local/bin/daemon")
