import time
import uuid
from dpath.util import new as dpnew
from dpath.util import set as dpset
from dpath.util import get as dpget
from typing import Generic, Callable, Iterator, TypeVar, Iterable, Sized, Any
from coref.internal.monad.internal import NONE
from .Dict import Dict
from oslash import Monad, Just

class Namespace(Dict):
    def __init__(self, derive: Callable[[Callable], Any]=None, **kw) -> None:
        if derive is None:
            self._value = {}
        elif isinstance(derive, dict) is True:
            self._value = derive
        elif isinstance(derive, Monad) is True and ( hasattr(derive, 'value') is True and isinstance(derive.value, dict) is True ):
            self._value = derive.value
        elif callable(derive) is True:
            self._value = derive()
        else:
            self._value = {}
        self._value.update(kw)
        if '__dir__' not in self.value.keys():
            _new = {
                '__dir__': True,
                '__stamp__': time.time(),
                '__name__': '/',
                '__id__': str(uuid.uuid4())
            }
            self._value.update(_new)

    def Name(self):
        return Just(self._value['__name__'])

    def isDir(self):
        return Just(self._value['__dir__'])

    def mkdir(self, path: str) -> 'Namespace':
        from coref.internal.path import expandPath
        from coref.internal.util import unique

        ns = self._value
        try:
            v = dpget(ns, path)
            return Namespace(v)
        except KeyError:
            for d in unique(expandPath(path)):
                try:
                    dpget(ns, d)
                except KeyError:
                    _new = {
                        '__dir__': True,
                        '__stamp__': time.time(),
                        '__name__': d,
                        '__id__': str(uuid.uuid4())
                    }
                    dpnew(ns, d, _new)
            return Namespace(dpget(ns, path))

    def cd(self, path: str) -> 'Namespace':
        ns = self._value
        try:
            return Namespace(dpget(ns, path))
        except KeyError:
            return self.mkdir(path)

    def V(self, path: str, value: Monad=NONE) -> Any:
        import os.path

        ns = self._value
        try:
            v = dpget(ns, path)
            if value is not NONE:
                dpset(ns, path, value.value)
                return value
            return Just(v)
        except KeyError:
            if value is NONE:
                return NONE
            self.mkdir(os.path.dirname(path))
            dpnew(ns, path, value.value)
            return Just(value.value)
