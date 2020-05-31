import time
import uuid
from coref.internal.dp import DP
from coref.internal.path import expandPath
from coref.internal.util import unique, partial
from typing import Generic, Callable, Iterator, TypeVar, Iterable, Sized, Any
from coref.internal.monad.internal import NONE
from .Dict import Dict
from oslash import Monad, Just, Nothing

class Namespace(Dict):
    def __init__(self, derive: Callable[[Callable], Any]=None, **kw) -> None:
        if derive is None:
            self._value = DP()
        elif isinstance(derive, dict) is True:
            self._value = DP(derive)
        elif isinstance(derive, Monad) is True and ( hasattr(derive, 'value') is True and isinstance(derive.value, dict) is True ):
            self._value = DP(derive.value)
        elif callable(derive) is True:
            self._value = derive()
        else:
            self._value = DP()
        for k in kw:
            v = kw[k]
            if isinstance(v, Monad) is True:
                self._value.raw()[k] = v.value
            else:
                self._value.raw()[k] = v
        if '__dir__' not in self._value.keys():
            _new = {
                '__dir__': True,
                '__stamp__': time.time(),
                '__name__': '/',
                '__id__': str(uuid.uuid4())
            }
            self._value.raw().update(_new)

    def append(self, other: 'Dict') -> 'Dict':
        if self.null():
            return other
        _d = self.empty()
        if hasattr(self, "parent") is True:
            _d.parent = self.parent
        _d.raw().raw().update(self.value.raw())
        if isinstance(other.value, DP) is True:
            _d.raw().raw().update(other.value.raw())
        else:
            _d.raw().raw().update(other.value)
        if hasattr(other, "parent") is True and hasattr(_d, "parent") is False:
            _d.parent = other.parent
        return (_d)

    def raw(self):
        return self._value

    def Name(self):
        return Just(self._value.raw()['__name__'])

    def isDir(self):
        return Just(self._value.raw()['__dir__'])

    def Mkdir(self, *path) -> tuple:
        _p = []
        _res = []
        for p in path:
            _p += expandPath(p)
        for i in unique(_p):
            _res.append(self.mkdir(i))
        return tuple(_res)

    def mkdir(self, path: str) -> 'Namespace':
        _nns = Namespace(self._value.mkdir(path))
        if hasattr(self, "parent") is True:
            _nns.parent = self.parent
        else:
            _nns.parent = self
        return _nns

    def Cd(self, *path) -> tuple:
        _res = []
        for i in unique(path):
            _res.append(self.cd(i))
        return tuple(_res)
    def cd(self, path: str) -> 'Namespace':
        ns = self._value
        try:
            res =  Namespace(self._value.get(path))
        except KeyError:
            res =  self.mkdir(path)
        if hasattr(self, "parent") is True:
            res.parent = self.parent
        else:
            res.parent = self
        return res

    def C(self):
        if hasattr(self, "parent"):
            self.parent.raw().set(self.Name().value, self._value)

    def V(self, path: str, value: Monad=NONE) -> Any:
        import os.path

        if path[0] != "/":
            path = f"/home/{path}"

        if value is NONE or value is None or value is Nothing():
            return self._value.get(path)
        else:
            if isinstance(value, Monad) is True:
                data = value.value
            else:
                data = value
            self._value.set(path, value)
            return value
        return NONE

    def f(self, name: str, *args, **kw) -> Any:
        def _fun(*args, **kw):
            return NONE
        path = self._value.get("/etc/path", ["/bin", "/home"])
        if name[0] == "/":
            fun = self._value.get(name, _fun)
            if args or kw:
                return partial(fun.value, *args, **kw)
            return fun.value
        else:
            for p in path.value:
                fname = f"{p}/{name}"
                fun = self._value.get(fname, None)
                if fun is not None:
                    if args or kw:
                        return partial(fun.value, *args, **kw)
                    return fun.value
        return _fun
