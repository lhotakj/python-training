def x():
    yield 10
    yield 20
y = x()
next(y)

# returns 10
next(y)
# returns 20

l = [x()]
# returns generator object

l = list(x())
l

# returns [10, 20]
for i in x():
    print i
