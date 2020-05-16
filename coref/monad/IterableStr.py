class IterableStr:
    def __str__(self):
        out = "["
        for v in super(self.__class__,self).getValue():
            out += "{} ".format(repr(v))
        out += "]"
        return out
