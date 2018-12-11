class X():
    def __init__(self, name):
        self.name = "X:{0}".format(name)

    def __str__(self):
        return self.name


class Y():
    def __init__(self, name):
        self.name = "Y:{0}".format(name)

    def __str__(self):
        return self.name

def class_factory(is_X):
    return X if is_X else Y

meta_class = class_factory(True)
x = meta_class("tom")
print(x)

meta_class = class_factory(False)
y = meta_class("petr")
print(y)

print(class_factory.__code__.co_argcount) # POCET ARGUMENTU FUNKCE

