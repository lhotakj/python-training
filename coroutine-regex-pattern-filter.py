import re
import asyncio #old in 2.7

# pattern filter ---------------

@asyncio.coroutine
def regex_matcher(regex):
    while True:
        text = (yield)
        print('Received: {0}'.format(text))
        for match in regex.finditer(text):
            print(match.group())

regex = re.compile('a+')
r = regex_matcher(regex)
x=next(r)
r.send('anaaconda')
r.send('ahoj')
r.send('pakarna')

