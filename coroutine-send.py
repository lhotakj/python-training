import asyncio  # old in 2.7

@asyncio.coroutine
def regex_matcher(receiver, regex):
    while True:
        text = (yield)
        for match in regex.finditer(text):
            receiver.send(match)


# Sending to coro! Example #1 -------------------
def coro():
    a = yield  'ahoj'
    yield a

c = coro()

print(type(c))
# type generator

print(next(c))
# ahoj

print(c.send('cau'))
# cau

print(c.send('cau'))
# stop iter!

# Sending to coro! Example #2 -------------------
def coro():
    a = yield 'ahoj'
    print(a)
    print(type(a))
    yield a

c = coro()
next(c)
# ahoj
c.send('cau')
