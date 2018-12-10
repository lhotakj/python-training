
class Flip(dict):
    def flip(self):
        res = {}
        for k in self:
            v = self[k]
            if not v in res:
                res[v] = set()
            res[v].add(k)
        return res

original = {'a':1, 'b':2, 'c':3, 'd':2, 'e':4}
ff = Flip(original)
flipped = ff.flip()
print(flipped)

# functor way --------------------------------------------------------------

class Flip(dict):
    def __call__(self):  # this is functor!
        res = {}
        for k in self:
            v = self[k]
            if not v in res:
                res[v] = set()
            res[v].add(k)
        return res

original = {'a':1, 'b':2, 'c':3, 'd':2, 'e':4}
ff = Flip(original)
flipped = ff()  # without .flip()
print(flipped)


