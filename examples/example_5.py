import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref.mod import *
from coref.internal.util import *
from coref.internal.monad import *
import pdb

def doubler(x):
    return x*2

ns = Namespace()
nsImport(ns, 'coref.stdlib')
print(ns)
