import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coref.monad import *
from coref.internal import *

def test_uniq_1():
    a = L('abc', 'abc', 'ab', 'bc')
    a = a & unique
    assert len(a) == 3

def test_expandpath_1():
    a = L('/a/b/c')
    a = (a | expandPath) & unique
    assert len(a) == 3
