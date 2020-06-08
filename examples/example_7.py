import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *

ns, f, F = NS()
print("args", nsGet(ns, "/etc/args"))
print("flags", nsGet(ns, "/etc/flags"))
print("default", nsGet(ns, "/etc/args/default"))
print("cmds", ns.dir("/etc/args"))
print("argv", nsGet(ns, "/etc/argv"))
