import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from oslash import *
from coref import *

def test_hylang_1():
    ns, f, F = NS()
    assert ns.V("/sys/hylang.enabled") == TRUE

def test_hylang_2():
    ns, f, F = NS()
    assert F("hy", "(+ 41 1)") == Right(42)

def test_hylang_3():
    ns, f, F = NS()
    assert f("hy|")("1 (+ 41)") == 42
