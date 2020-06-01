import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref.internal.v import *
from coref.internal.util import partial

def test_monad_V_1():
    d = Vstor()
    d.mount('home', ':mem:', ['/home/*'])
    assert d.read('home', '/__sys/__ready__')

def test_monad_V_2():
    d = Vstor()
    d.mount('home', ':mem:', ['/home/*'])
    assert d.set("/home/answer", 42) == 42

def test_monad_V_3():
    d = Vstor()
    d.mount('home', ':mem:', ['/home/*'])
    d.set("/home/answer", 42)
    assert d.get("/home/answer") == 42

def test_monad_V_4():
    d = Vstor()
    d.mount('home', ':mem:', ['/home/*'])
    assert d.here("/home/answer")
