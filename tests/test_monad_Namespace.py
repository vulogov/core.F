import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from oslash import *
from coref.internal.monad import *


def test_monad_Namespace_1():
    d = Namespace()
    assert d.null() == False

def test_monad_Namespace_2():
    d = Namespace()
    d.V('/answer', Just(42))
    assert d.V('/answer') == Just(42)

def test_monad_Namespace_3():
    d = Namespace()
    assert d.V('/answer') == NONE

def test_monad_Namespace_4():
    d = Namespace()
    assert d.Name() == Just("/")

def test_monad_Namespace_5():
    d = Namespace()
    assert d.isDir() == TRUE

def test_monad_Namespace_6():
    d = Namespace()
    d.V('/home/answer', Just(42))
    home = d.cd('/home')
    assert home.Name() == Just("/home")

def test_monad_Namespace_7():
    d = Namespace()
    d.V('/home/answer', Just(42))
    home = d.cd('/home')
    assert home.V("/answer") == Just(42)
