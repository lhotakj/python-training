class Person(object):
    pass

x = Person()
print(type(x))  # module __main__.Person in Py3 , but instance in Py2!!! to make it compatible use Person(object)
# new-style of classes!
# py2 doesn't inherit! https://www.python.org/doc/newstyle/
# use in py2/py3 (object)!!!

print(dir(x))
x.neco = 123   # new attribute without changing class!

print(dir(x))


