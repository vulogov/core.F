import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from oslash import *
from coref.internal.monad import *

def doubler(x):
    return x*2

def test_monad_Dict_1():
    d = Dict()
    assert d.null() == True

def test_monad_Dict_2():
    d = Dict(answer=42)
    assert d["answer"] == 42

def test_monad_Dict_3():
    d = Dict(answer=42)
    del d["answer"]
    assert d.null() == True

def test_monad_Dict_4():
    d = Dict(answer=21)
    d = d | doubler
    assert d["answer"] == 42

def test_monad_Dict_5():
    d = Dict(doubler=doubler)
    r = d * Dict(answer=21)
    assert r["answer"] == 42

def test_monad_Dict_6():
    assert Dict(answer=42) == Dict(answer=42)

def test_monad_Dict_7():
    d = Dict() + Values(answer=42)
    assert d["answer"] == 42
