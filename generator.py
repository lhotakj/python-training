
def firstn(n):
    num = 0
    while num < n:
        yield num # yield like return
        num += 1


# generator - simple way of creating data
sum_of_first_n = sum(firstn(100))
print(sum_of_first_n)

# or Tomas's way :)
x = firstn(100)
print(next(x))
print(next(x))
print(next(x))