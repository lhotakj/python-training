
# de facto decorator
def f1(p):
    def f2():
        print(p)
    return f2()

x = f1('cau')
print(type(x))
# <class 'function'>

print(x())
# cau

print(f1('xxx'))
# Error: NameError: name `f1` not defined
