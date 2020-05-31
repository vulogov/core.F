import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from oslash import *
from coref.internal.monad import *

def doubler(x):
    return x*2

def test_monad_L_1():
    l = L()
    assert l.null()

def test_monad_L_2():
    l = L([21]) | doubler
    assert l.head() == 42
