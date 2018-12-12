#imperative vs. oop vs. functional
#imperative
s=0
for n in range(1, 10):
  if n%3==0 or n%5==0:
    s+=n
print(s)


#oop
m=list()
for n in range(1, 10):
  if n%3==0 or n%5==0:
    m.append(n)
print(sum(m))

#functional
def until(n, filter_func, v):
  if v == n:
    return []
  if filter_func(v):
    return [v] + until( n, filter_func, v+1 )
  else:
    return until(n, filter_func, v+1)

mult_3_5= lambda x: x%3==0 or x%5==0
until(10, lambda x: x%3==0 or x%5==0, 0)

