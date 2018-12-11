#!/usr/bin/env python3.3
class FlipDict(dict):
  def flip(self):
    res = {}
    for k in self:
      v = self[k]
      if not v in res:
        res[v] = set()
      res[v].add(k)
    return res
  def test(self):
    print(id(self))
    a=FlipDict({1:2})
    print(id(a))
    self=a
    print(id(self))
    

x=FlipDict({1:'a',2:'b',3:'a'})
print(x)
y=x.flip()
print(y)
x.test()
print(x.keys())
