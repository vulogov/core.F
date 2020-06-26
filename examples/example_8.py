import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *

def appconfig(ns):
    print("Application config")

ns, f, F = NS()
res = F("/dev/console/send", "Hello, console!")
print(ns.V("/home/NotAnswer"))
print(res)
F("/bin/initAppRegister", appconfig, level=1, action='start')
F("/bin/main")
