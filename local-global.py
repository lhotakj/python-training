# using  global
# ----------------

def x():
    global a
    print("globals() = " + str(globals()))
    a = 10
    b = 20
    print('a=' + str(a))
    print('b=' + str(b))

a=33
x()

# ------------------------------------------------------------------
# and now error

def x():
    a = 10
    b = 20
    print('b = ' + str(b))

a = 33
x()
# error: UnboundLocalError: local variable 'a' referenced before assignment

