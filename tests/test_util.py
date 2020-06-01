import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *
from coref.internal.util import mergedicts

def test_util_1():
    a={'a':{'b':42}}
    b={'a':{'pi':3.14}}
    a = mergedicts(a,b)
    assert a['a']['pi'] == 3.14
