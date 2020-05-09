import os.path

def expandPath(x):
    p = os.path.normpath(x)
    _p = p.split("/")
    _p = [i for i in _p if i]
    out = []
    for e in reversed(range(len(_p))):
        _d = "/"+"/".join(_p[:(e+1)])
        out.append(_d)
    return out
