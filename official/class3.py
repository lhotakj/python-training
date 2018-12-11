class A(object):
    def __init__(self, **kwargs):
        print('A init')
        super().__init__()

class B(A):
    def __init__(self, **kwargs):
        print('B init {}'.format(kwargs['x']))
        super().__init__(**kwargs)


class C(A):
    def __init__(self, **kwargs):
        print('C init {}, {}'.format(kwargs['a'], kwargs['b']))
        super().__init__(**kwargs)


class D(B, C):
    def __init__(self):
        print('D init')
        super().__init__(a=1, b=2, x=3)

print(D.mro())
o=D()
