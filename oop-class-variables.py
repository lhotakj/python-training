class Person:

    Person_id=1

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.cid=Person.Person_id
        Person.Person_id+=1

    def printall(self):
        print ("Name : %s, age : %d, id : %d" % (self.name,self.age,self.cid))


bob=Person("Bob",20)
alice=Person("Alice",19)
bob.printall()
alice.printall()