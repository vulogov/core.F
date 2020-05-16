from .OrOp import OrOp
from pymonad.Maybe import _Nothing
from pymonad.Monoid import *

class _NONE(_Nothing, OrOp):
    def __str__(self):
        return "NONE"

    def bind(self, function):
        return NONE()

NONE = _NONE()
