class Person:
    Person_id=1

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.cid=Person.Person_id
        Person.Person_id+=1

    @classmethod
    def resetPerson(cls):
        cls.Person_id=1

    #resetPerson=classmethod(resetPerson) #! classmethod reference --> old way
                                         # now used by @classmethod

    def printall(self):
        print ("Name : %s, age : %d, id : %d" % (self.name,self.age,self.cid))

    @classmethod
    def Test(cls):
        print('calling Test (class method) ' + str(cls))

    @staticmethod
    def TestStatic(x):
        print('calling static Test (static method) ' + str(x))
        # I can see only stuff from class definition
        print('list of what I can see')
        print(dir())



p = Person('a',1)
p.Test()
Person.TestStatic(1)



bob=Person("Bob",20)
bob.resetPerson()

alice=Person("Alice",19)
bob.printall()
alice.printall()