import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pymonad import curry
from coref.ns import *

def test_ns_1():
    ns = fNS()
    L("/bin","/sys") | curry(fMkdir)(ns)
    assert "bin" in ns.ls()
