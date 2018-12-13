def regex_matcher(receiver, regex):
    while True:
        text = (yield)
        for match in regex.finditer(text):
            receiver.send(match)

def msf(x, text):
    x.send(text)
    while True:
        l = yield
        print(l)

r = regex_matcher(ms, 'a+')
ms = msf(r, 'anaaconda')
