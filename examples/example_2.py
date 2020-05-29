import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from functools import partial
from coref.internal.monad import *


d = Namespace()
print (d)
print (d.V("/answer", Just(42)))
print (d.value)
