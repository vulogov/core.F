import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from functools import partial
from coref.internal.monad import *
import pdb


d = Namespace()
print (d)
print ("Set()",d.V("/answer", Just(42)))
print ("After Set()", d)
print ("Get()",d.V("/answer"))
print ("Set()",d.V("/home/answer", Just(42)))
home = d.cd("/home")
print ("Home()", home)
print ("Home(Set())", home.V("/pi", 3.14))
print ("Home()", home)
print ("Home().parent", home.parent)
home.C()
print ("After C()", d)
print ("mkdir()", d.mkdir("/usr/local/bin"))
print ("After mkdir()", d)
print ("f()", d.f("/bin/doubler"), d.f("/bin/doubler")())
