#!/usr/bin/env python

class typeEnforcer(object):
    def __init__(self, *args):
        self.typeTuple = args

    def __call__(self, f):
        def wrapped_f(*args):
            if len(self.typeTuple) != len(args):
                raise Exception("Expected type is not the same length as *args")
            for a, t in zip(args, self.typeTuple):
                if type(a) != t:
                    raise Exception("%s is type %s, not expected type %s" % (a, type(a), t) )
            return f(*args)
        return wrapped_f


@typeEnforcer(int)
def xequalsxplusone(x):
    return x + 1

@typeEnforcer(int, int)
def addition(a, b):
    return a + b

@typeEnforcer(str, int)
def stringmultiplication(string, multiplier):
    result = ""
    for i in range(multiplier):
        result += string
    return result

# good data
print xequalsxplusone(2)
print addition(5, 8)
print stringmultiplication("test", 5)

# bad data
try:
    print xequalsxplusone({"hello": "world"})
except Exception, e:
    print e
try:
    print addition(5.5, "what")
except Exception, e:
    print e
try:
    print stringmultiplication(5, "test")
except Exception, e:
    print e
