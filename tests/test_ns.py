import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pymonad import curry
from coref.ns import *

def test_ns_1():
    f, ns = fNS()
    L("/bin","/sys") | curry(fMkdir)(ns)
    assert "bin" in ns.ls()

def test_ns_2():
    def test_fun(ns, x):
        return x
    f, ns = fNS()
    I(ns, "/bin/echo", test_fun)
    assert "echo" in ns["bin"].keys()

def test_ns_3():
    def test_fun(ns, x):
        return x
    f, ns = fNS()
    I(ns, "/bin/echo", test_fun)
    assert ns["bin"]["echo"](42) == 42

def test_ns_4():
    def test_fun(ns, x):
        return x
    f, ns = fNS()
    I(ns, "/bin/echo", test_fun)
    f("/bin/echo")
