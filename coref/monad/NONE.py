from pymonad.Maybe import _Nothing
from pymonad.Monoid import *

class _NONE(_Nothing):
    def __str__(self):
        return "NONE"

    def bind(self, function):
        return None()

    def __or__(self, function):
        return super(None, self).__rshift__(function)

NONE = _NONE()
