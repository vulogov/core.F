import os.path
import pkgutil
import importlib
from oslash import Monad
from coref.internal.monad import *
from coref.internal.util import partial

def nsList(*elem) -> 'L':
    return L(list(elem))

def nsValues(*elem, **values):
    _nns = Dict()
    for e in elem:
        if isinstance(e, dict) is True:
            _nns += Dict(e)
    _nns += Dict(values)
    return _nns

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['-q', 'install', '-U', '--compile', '--force-reinstall', '--user', package])
    finally:
        globals()[package] = importlib.import_module(package)

def nsImport(ns, m, *_mods):
    if type(m) == list and len(m) > 0:
        for _m in m:
            ns = _nsImport(ns, _m)
    elif type(m) == str:
        return _nsImport(ns, m)
    else:
        for _m in _mods:
            ns = _nsImport(ns, _mod)
        return ns
    return ns

def I(ns, name, fun):
    return nsSet(ns, name, partial(fun, ns))

def _nsImportAttribute(ns, _module, attr):
    if hasattr(_module, attr) is True:
        v = getattr(_module, attr)
        if isNothing(v) is True:
            return NONE
        if isinstance(v, Monad):
            return v
        if isinstance(v, dict):
            return Dict(v)
        if isinstance(v, list):
            return L(v)
    return NONE

def _nsImportModule(ns, _module):
    _attrs = ['_lib', '_mkdir', '_ln', '_init', '_set', '_ctx', '_ns', '_tpl']
    _mod = Dict()
    for a in _attrs:
        _mod[a] = _nsImportAttribute(ns, _module, a)
    return _mod

def _nsImportSet(ns, d):
    if isNothing(d) is True:
        return
    for k,v in d:
        ns.V(k, v)

def _nsImportMkdir(ns, d):
    if isNothing(d) is True:
        return
    def _nsMkdir(ns, x):
        ns.mkdir(x)
    mkdir = partial(_nsMkdir, ns)
    d | mkdir

def _nsImportTpl(ns, d):
    if isNothing(d) is True:
        return

def _nsImportLib(ns, d):
    if isNothing(d) is True:
        return
    for k,v in d:
        ns.V(k, partial(v, ns))


def _nsImport(ns, module):
    for loader, module_name, is_pkg in pkgutil.walk_packages(importlib.import_module(module).__path__):
        _module = loader.find_module(module_name).load_module(module_name)
        _mod = _nsImportModule(ns, _module)
        _nsImportMkdir(ns, _mod["_mkdir"])
        _nsImportSet(ns, _mod["_set"])
        _nsImportLib(ns, _mod["_lib"])
        _nsImportLib(ns, _mod["_tpl"])
    return ns
