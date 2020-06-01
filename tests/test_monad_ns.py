import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *

def test_ns_1():
    ns = Namespace()
    nsSet(ns, "/home/answer", 42)
    assert nsGet(ns, "/home/answer") == Just(42)
