class OrOp:
    def __or__(self, function):
        return super(self.__class__, self).__rshift__(function)
