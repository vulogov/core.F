import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coref.internal.util import *
from coref.internal.monad import *
import pdb

def doubler(x):
    return x*2

l = L()
l = l.cons(42)
print ("repr()",repr(l))
l = l.cons(3.14)
print ("l.value", l.value)
print ("l.raw()", l.raw())
print ("L()", l)
l += L(["hello"])
print ("L()", l)
nums = L([1,2,3])
nums = nums | doubler
print ("L(nums)",nums)
