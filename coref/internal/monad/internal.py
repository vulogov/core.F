from .Dict import Dict
from oslash.list import List
from oslash.maybe import Just, Nothing

Value = Just
Values = Dict
NONE=Nothing()
TRUE=Just(True)
FALSE=Just(False)

def isNothing(x):
    return x == None or x == NONE or x == Nothing()
