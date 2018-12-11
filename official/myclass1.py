class MyClass():
  def __init__(self,name,age):
    self.name=name
    self.age=age
    self.__prom=555
  @classmethod
  def reset(cls):
    print('reset method called')
    print(cls)
    print(dir())
    pass
  @staticmethod
  def stat(x):
    print(dir())
    pass

a=MyClass('a',123)
MyClass.reset()
a.stat(123)
print(a._MyClass__prom)
