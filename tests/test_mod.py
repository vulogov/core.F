import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *

def test_mod_1():
    d = nsValues({
        'pi': 3.14
    }, answer=42)
    assert d['answer'] == 42

def test_mod_2():
    d = nsValues({
        'pi': 3.14
    }, answer=42)
    assert d['pi'] == 3.14
