import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coref.ns import *

def test_ns_1():
    V = fNS()
    assert len(V("/").getValue()) == 3
