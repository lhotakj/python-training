class o:

    def __init__(self):
        self.x = 1
        self._x = 2
        self.__x = 3

obj = o()

print(obj.x)   # 1
print(obj._x)  # 2
# print(obj.__x) # fails

print(dir(obj))

# use this
print(obj._o__x) # 2