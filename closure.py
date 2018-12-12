# closure - uraverove fuknmce

a = 10
def f1():
    nonlocal a
    pass

# error - no binding for nonlocal 'a' found ;)

def f1():
    b=123
    def f2():
        nonlocal b
        pass

# OK

