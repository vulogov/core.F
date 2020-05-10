import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coref.monad import *

def test_ns_1():
    d = Namespace()
    d += Namespace(answer=42)
    assert d['answer'] == 42

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

def test_dict_4():
    def doubler(x):
        res = {}
        for k in x:
            res[k] = x[k]*2
        return res
    d = Dict(answer=21) | doubler | doubler
    assert d['answer'] == 84

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

def test_set_4():
    def doubler(x):
        return x*2
    s = Set(21) | doubler
    assert 42 in s

def test_value_1():
    val = Value(42)
    assert val.getValue() == 42

def test_value_2():
    val = Value(21) + Value(21)
    assert val.getValue() == 42

def test_value_3():
    def doubler(x):
        return x*2
    val = Value(21) | doubler
    assert val.getValue() == 42

def test_value_4():
    val = Value(42)
    assert val == v(42)

def test_value_5():
    val = Value(42) == 42
    assert val == TRUE

def test_value_6():
    val = Value(42) == 41
    assert val == FALSE

def test_v_1():
    d = v(42)
    assert d.getValue() == 42

def test_v_2():
    d = v([1,2,3])
    assert len(d) == 3

def test_v_3():
    d = v(1,2,3)
    assert len(d) == 3

def test_v_4():
    d = v(answer=42)
    assert d["answer"] == 42

def test_v_5():
    d = v(set([1,2,3]))
    assert len(d) == 3

def test_v_5():
    assert v(True) == TRUE
