import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from functools import partial
from coref.internal.monad import *
import pdb


d = Namespace()
print (d)
print (d.V("/answer", Just(42)))
print (d.value)
print (d.V("/home/answer", Just(42)))
home = d.cd("/home")
print("Parent exists",home.parent)
#pdb.run("home = home + Values(pi=3.14)")
home = home + Values(pi=3.14)
print("This is home",home)
print("This is home parent", home.parent)
home.C()
print("Committed changes in parent namespace",d)
print("Making dirs", d.Mkdir('/home', '/usr/local', '/etc', '/etc/init.d'))
print("Getting dirs", d.Cd('/home', '/usr/local', '/etc', '/etc/init.d'))

d = Namespace()
home = d.mkdir('/home')
home += Values(answer = 42)
print("+Values()",home)
home.C()
print("After C()", d)

def Doubler(ns, path):
    return ns.V(path) * 2

d = Namespace()
d.V("/home/answer", 42)
d.V("/bin/doubler", Doubler)
print(d.raw())
print(d.raw()["bin"]["doubler"],d.V("/bin/doubler"))
#print("With doubler", d.V("/bin/doubler"))
