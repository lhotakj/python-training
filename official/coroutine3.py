import re
def regex_matcher(regex):
    while True:
        text = (yield)
        print('Received '+text)
        for match in regex.finditer(text):
            print(match.group())
            #print(dir(match))

regex = re.compile('a+')
r = regex_matcher(regex)
x = next(r)
#print(x)
r.send('anaaconda')
r.send('ahoj')
