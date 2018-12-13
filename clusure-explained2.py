
# closure as multiplicatpr
def nasobek_n(n):
    def inner(x):
        nonlocal n  # optionally
        return x*n
    return inner()


krat3 = nasobek_n(3)
krat5 = nasobek_n(5)

print(krat3(7))
# 21

print(krat5(5))
# 35

print(krat5(krat3(4)))
# 68

dir(krat3.__closure__)
# < cell at ..... int object ....> = depends on an int, in this case "3"
# the function can be bound to any object, lambda or other function
# in case I'd delete the reference, the function would still work (refdefcount would decrease)

