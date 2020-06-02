import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from oslash import *
from coref.internal.monad import *


def test_monad_Tpl_1():
    ns = Namespace()
    ns.V("/home/answer", Just(42))
    assert Tpl("$home.answer")(ns) == "42"
