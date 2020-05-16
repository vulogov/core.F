from .IterableStr import IterableStr
from .OrOp import OrOp
from pymonad.List import List

class L(List, IterableStr, OrOp):
    def __and__(self, function):
        return L(*function(self.getValue()))
    def bind(self, function):
        result = []
        for subList in (map(function, self)):
        	result.extend(subList)
        return L(*result)
