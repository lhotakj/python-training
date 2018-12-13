class B():
    def __init__(self, name):
        self.name = name
        print('called B init')
        pass

class C():
    def __init__(self, age):
        self.age = age
        print('called C init')
        pass

class D(B, C):
    def __init__(self, n, a):
        B.__init__(self, n)
        C.__init__(self, a)
        pass

o = D('Jan', 23)
print(dir(o))
