
def f(a, L=[]):
     L.append(a)
     return L

print(f.__defaults__)
# ([],)
print(f(10))
# [10]
print(f.__defaults__)
# ([10],)
