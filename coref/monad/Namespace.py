import re
from .Dict import Dict
from .L import L

class Namespace(Dict):
    def ls(self):
        return L(*[item for item in list(self.getValue().keys()) if re.match(r"^(?!\_\_.*)", item)])

    def __str__(self):
        x = self.getValue()
        return "Namespace[{}]: {}".format(x.get('__name__', 'UNKNOWN'), self.ls())

    def mplus(self, other):
        super(Namespace, self).update(other)
        return Namespace(**self)

    def __or__(self, function):
        return super(Namespace, self).__rshift__(function)

    def bind(self, function):
        return Namespace(**function(self))

    @staticmethod
    def mzero():
        return Namespace()

    def fmap(self, function):
        res = {}
        for k in self:
        	res[k] = function(k, self[k])
        return Namespace(**res)

    def amap(self, functorValue):
        result = {}
        for name in self.getValue():
        	result[name] = self[key] * functorValue
        return Namespace(**result)

    def __and__(self, function):
        return Namespace(**function(self.getValue()))