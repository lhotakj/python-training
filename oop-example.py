class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):   # shoul look similar to __repr__
        return(self.name)

    def __repr__(self):   # used for REPL console!
        return("[" + self.name + "]")

    def __gt__(self, other):
        if (self.age > other.age):
            return True
        return False

    def __add__(self, other):
        return self.age + other.age  # should contains type check ! using isInstance :)

    def printall(self):
        print("Name: % s, age: % d " % (self.name,self.age))

bob = Person("Bob", 20)
alice = Person("Alice", 19)
print(bob + alice)

print(bob.__getattribute__('printall'))
print(dir(bob.__getattribute__('printall')))
#print(bob.__getattribute__('printall'))
