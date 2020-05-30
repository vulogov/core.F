def unique(x: list) -> list:
    return list(set(x))

def partial(func, *args, **keywords):
    def f(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    f.func = func
    f.args = args
    f.keywords = keywords
    f.__name__ = func.__name__
    return f
