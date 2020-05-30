import os.path
import time
import uuid
from oslash import Monad
from oslash.maybe import Just, Nothing

class DP:
    def __init__(self, *derive, **kw):
        self._value = {}
        for d in derive:
            if callable(d) is True:
                self._value.update(d())
            if isinstance(d, dict) is True:
                self._value.update(d)
        self._value.update(kw)
        if '__name__' not in self._value.keys():
            self._value.update(
                {
                    '__name__': '/',
                    '__stamp__': time.time(),
                    '__dir__': True,
                    '__id__': str(uuid.uuid4())
                }
            )
    def __len__(self):
        return len(self._value.keys())

    def keys(self):
        return self._value.keys()

    def mkdir(self, path):
        _p = os.path.abspath(path).split("/")
        _p = [i for i in _p if i]
        return self._mkdir_(_p, [""], self._value)

    def _mkdir_(self, _p, _fp, _d):
        if len(_p) == 0:
            return _d
        name = _p[0]
        _fp.append(name)
        if name in _d.keys():
            d = _d[name]
        else:
            d = self._mkdir(_d, name, _fp)
        return self._mkdir_(_p[1:], _fp, d)

    def _mkdir(self, _d, name, _fp):
        fp = "/".join(_fp)
        _d[name] = {
            '__name__': fp,
            '__stamp__': time.time(),
            '__dir__': True,
            '__id__': str(uuid.uuid4())
        }
        return _d[name]

    def set(self, path, value):
        _p = os.path.abspath(path).split("/")
        _p = [i for i in _p if i]
        return self._set(_p, [""], self._value, value)

    def _set(self, _p, _fp, _d, value):
        if len(_p) == 1:
            if isinstance(value, Monad) is True:
                _d[_p[0]] = value.value
                return value
            else:
                _d[_p[0]] = value
                return Just(value)
        d = _d.get(_p[0], None)
        if _d.get(_p[0], None) is None:
            _fp.append(_p[0])
            d = self._mkdir(_d, _p[0], _fp)
        return self._set(_p[1:], _fp, d, value)

    def get(self, path, default=Nothing()):
        _p = os.path.abspath(path).split("/")
        _p = [i for i in _p if i]
        return self._get(_p, [""], self._value, default)

    def _get(self, _p, _fp, _d, default):
        if len(_p) == 1:
            try:
                if isinstance(_d, dict) is True:
                    return Just(_d[_p[0]])
                if isinstance(_d, DP) is True:
                    return Just(_d.raw()[_p[0]])
                else:
                    return Nothing()
            except KeyError:
                if isinstance(default, Monad) is True:
                    return default
                else:
                    return Just(default)
        d = _d.get(_p[0], None)
        if _d.get(_p[0], None) is None:
            _fp.append(_p[0])
            d = self._mkdir(_d, _p[0], _fp)
        return self._get(_p[1:], _fp, d, default)

    def raw(self):
        return self._value

    def __repr__(self):
        return str(self._value)