def nasobek_n(n):
    def inner(x):
        return x*n
    return inner

krat3 = nasobek_n(3)
krat5 = nasobek_n(5)
print(krat3(7))
#21
print(krat5(7))
#35
print(krat5(krat3(4)))
#60
