from dpath.util import new as dpnew
from dpath.util import set as dpset
from dpath.util import get as dpget
from typing import Generic, Callable, Iterator, TypeVar, Iterable, Sized, Any
from coref.internal.monad.internal import NONE
from .Dict import Dict

class Namespace(Dict):
    def V(self, path: str, value: Any=NONE) -> Any:
        return NONE
