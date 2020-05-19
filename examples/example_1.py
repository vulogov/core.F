import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from functools import partial
from coref.internal.monad import *

def n(ns, x):
    return x

def a(*args):
    print("a()", args)
    return args

d = Dict(answer=42)
print(".null()",d.null())
print(".value", d.value)
d["pi"] = 3.14
print("pi",d["pi"])
d["n"] = n
d["pn"] = partial(n, d)
print(d["n"], d["pn"])
d2 = d | a
print("d2",d2)
d3 = d * Dict(value=1)
print("d3", str(d3))
