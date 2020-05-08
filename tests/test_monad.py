import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coref.monad.Dict import *

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
