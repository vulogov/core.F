import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coref.monad import *


def test_dict_1():
    d = Dict()
    d += Dict(answer=42)
    assert d['answer'] == 42

def test_dict_2():
    def echo(d):
        return d
    d = Dict(answer=42)
    d.bind(echo)
    assert d['answer'] == 42

def test_dict_3():
    def doubler(k,v):
        return v*2
    d = Dict(answer=21)
    d = d.fmap(doubler)
    assert d['answer'] == 42

def test_set_1():
    s = Set()
    s += Set(1,2,3)
    assert len(s) == 3

def test_set_2():
    def echo(d):
        return d
    s = Set(42)
    s.bind(echo)
    assert 42 in s

def test_set_3():
    def doubler(x):
        return x*2
    s = Set(21)
    s = s.fmap(doubler)
    assert 42 in s

def test_set_4():
    def doubler(x):
        return x*2
    s = Set(21) >> doubler
    assert 42 in s
