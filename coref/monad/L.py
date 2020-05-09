from pymonad.List import List

class L(List):
    def __or__(self, function):
        return super(L, self).__rshift__(function)
