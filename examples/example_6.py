import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref import *

ns, f, F = NS()
print ("F(/bin/time)", F("/bin/time").value)
print ("f(/bin/time)", f("/bin/time")())
