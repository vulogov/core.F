from pymonad.Maybe import *
from pymonad.Monoid import *

class Value(Just):
    def __str__(self):
        return str(self.getValue())

    def bind(self, function):
        return Value(function(self.getValue()))

    def __or__(self, function):
        return super(Value, self).__rshift__(function)

    def __and__(self, function):
        return super(Value, self).bind(function)

    def __eq__(self, other):
        if isinstance(other, Monad):
            return super(Value, self).getValue() == other.getValue()
        return super(Value, self).getValue() == other

    def __ne__(self, other):
        if isinstance(other, Monad):
            return super(Value, self).getValue() != other.getValue()
        return super(Value, self).getValue() != other


TRUE = Value(True)
FALSE = Value(False)
