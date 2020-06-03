import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref.mod import *
from coref.internal.util import *
from coref.internal.monad import *
import pdb

def doubler(x):
    return x*2

def divider(ns, x, y):
    return x/y

ns = Namespace()
nsImport(ns, 'coref.stdlib')
print ("/bin/time", ns.f("time")())
ns.V("/bin/divider", partial(divider, ns))
v = ns.F("/bin/divider", 2, 0)
print("division on 0", v.value)
print("traceback buffer", ns.V('/sys/traceback/tb'))
v = ns.F("/bin/divider", 4, 2)
print ("F()", v.value)
print ("trace buffer", ns.V('/sys/traceback/ftrace'))
