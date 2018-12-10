class X:
    pass

class Y:
    pass

class Z(X, Y):
    pass


# class C inherits A and B
#
#   [ X ]     [ X ]
#      \       /
#       \     /
#        \   /
#        [ Z ]

# real example
#
#        [ person ]
#        /    |    \
#       /     |     \
#    [man] [child] [woman]


# Resolution
#        [ X ]
#       /      \
#   [ A ]     [ B ]
#      \       /
#       \     /
#        \   /
#        [ C ]
#
# py2 C->A->X
# py3 C->A->B->X

class A():
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

print(D.mro())
# returns
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# mro c3

#-----------------------------------

class A(object):
    def __init__(self, name):
        self.name = name

class B(object):
    def __init__(self, age):
        self.age = age

# two in
class C(A, B):
    def __init__(self, name, age):
        #print(dir(super() ))
        A.__init__(self, name)
        B.__init__(self, age)


c = C("Jan",50)