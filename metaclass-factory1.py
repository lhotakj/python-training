

# define factory
print('-- create factory -------------')
factory = type('Factory', (), {'param1': 1})

print('factory :      ' + str(factory))
print('type(factory): ' + str(type(factory)))

print('\n-- create instance -------------')
f = factory()
print('f :            ' + str(f))
print('type(f):       ' + str(type(f)))
print('dir(f):        ' + str(dir(f)))

# in f() exists propety 'param1'
