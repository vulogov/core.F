from pymonad.List import List

class L(List):
    def __str__(self):
        out = "["
        for v in super(L,self).getValue():
            out += "{} ".format(repr(v))
        out += "]"
        return out
    def __or__(self, function):
        return super(L, self).__rshift__(function)
    def __and__(self, function):
        return L(*function(self.getValue()))
    def bind(self, function):
        result = []
        for subList in (map(function, self)):
        	result.extend(subList)
        return L(*result)
