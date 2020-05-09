from pymonad.Maybe import *
from pymonad.Monoid import *

class Value(Just):
    def __str__(self):
        return str(self.getValue())

    def bind(self, function):
        return Value(function(self.getValue()))
    
    def __or__(self, function):
        return super(Just, self).__rshift__(function)
