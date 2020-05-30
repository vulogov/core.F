import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref.internal.dp import *
from coref.internal.util import partial

def a(x, y):
    return x+y

def test_monad_DP_1():
    d = DP()
    assert len(d) == 4

def test_monad_DP_2():
    d = DP()
    d.set("/home/my/answer", 42)
    assert d.get("/home/my/answer") == Just(42)

def test_monad_DP_3():
    d = DP()
    d.set("/home/my/answer", Just(42))
    assert d.get("/home/my/answer") == Just(42)

def test_monad_DP_4():
    d = DP()
    d.set("/bin/add", Just(a))
    assert d.get("/bin/add") == Just(a)

def test_monad_DP_5():
    d = DP()
    d.set("/bin/add", a)
    assert d.get("/bin/add") == Just(a)

def test_monad_DP_6():
    d = DP()
    d.set("/bin/add", Just(partial(a, 2)))
    assert d.get("/bin/add").value(2) == 4
