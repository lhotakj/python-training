*REPL*:
Read Evaluate Print Loop - terminal :)

*Immutable vs Mutable*:
- Python handles mutable and immutable objects differently.
- Immutable are quicker to access than mutable objects.
- Mutable objects are great to use when you need to change the size of the object, example list, dict etc.. Immutables are used when you need to ensure that the object you made will always stay the same.
- Immutable objects are fundamentally expensive to “change”, because doing so involves creating a copy. Changing mutable objects is cheap.

*Adresa pameti*:
```i = 1
id(i)
i =+ 1
id(1)
```
other address! immutable!

*Build In*:
https://docs.python.org/3/library/functions.html

```
dir(s)
str(type(s)) - stringify
```

*Python language reference*:
https://docs.python.org/3/reference/

Kdyz napisu jen promemou zavola se `__repr__`! Wrapper 
Compound statements: if, else, elif

*List comprehension*
Generovani seznamu, slicing  `l[1:3:krok]` ...

```
i = 1
print(i.__class__)
```

Class == kompilacni template

Cpython - referenci implementace 

```
import sys
sys.getrefcount(object) #-- Returns the reference count of the object.
```

# Shelve & pickle

`pickle` is for serializing some object (or objects) as a single bytestream in a file.

`shelve` builds on top of pickle and implements a serialization dictionary where objects are pickled, but associated with a key (some string), so you can load your shelved data file and access your pickled objects via keys. This could be more convenient were you to be serializing many objects.

```
import pickle
integers = [1, 2, 3, 4, 5]

with open('pickle-example.p', 'wb') as pfile:
    pickle.dump(integers, pfile)
```
This will dump the integers list to a binary file called pickle-example.p.

Now try reading the pickled file back.

```
import pickle

with open('pickle-example.p', 'rb') as pfile:
    integers = pickle.load(pfile)
    print integers
```
The above should output `[1, 2, 3, 4, 5]`.

```
shelve Example
import shelve

integers = [1, 2, 3, 4, 5]
with shelve.open('shelf-example', 'c') as shelf:
    shelf['ints'] = integers
```
Notice how you add objects to the shelf via dictionary-like access.
Read the object back in with code like the following:

```
import shelve
with shelve.open('shelf-example', 'r') as shelf:
    for key in shelf.keys():
        print(repr(key), repr(shelf[key])))
```
The output will be `'ints', [1, 2, 3, 4, 5]`.

# Coroutines
Coroutines are functions whose processing can be suspended and resumed at specific points. So, typically, a coroutine will execute up to a certain statement, then suspend execution while waiting for some data. At this point other parts of the program can continue to execute (usually other coroutines that aren’t suspended). 

I can *write* into couroutines using `.send()`, but generators are for *read* only
Leads to multi-thread porgramming, *waiting* = `yeild` 
It's like a function with `return` but wrapped into an iterable envelope!!

```
def x():
    yield 10
    yield 20
y=x()
next(y)
# returns 10
next(y)
# returns 20
l=[x()]
# returns generator object
l=list(x())
l
# returns [10, 20]
for i in x() print i
```
Note that cpython doesn't do well threads (shared memory!)
Old way in python2.7 `@asyncio.coroutine`

![img](/pdf/tulip_coro.png)

# Meta class
Used like for factory!

```
class X():
    pass

def f1():
    x=X()
    return x

def f2()
    return X
y = f()
type(y)
# <class '__main__.X'>
y = f2()
type(y)
# <class 'type'> ===> metaclass

yy=y()
type(yy)  
# <class '__main__.X'>
```

Note we can use alseo build-in function `type`!

```
# define factory
print('-- create factory -------------')
factory = type('Factory', (), {'param1':1})

print('factory :      ' + str(factory))
print('type(factory): ' + str(type(factory)))

print('\n-- create instance -------------')
f = factory()
print('f :            ' + str(f))
print('type(f):       ' + str(type(f)))
print('dir(f):        ' + str(dir(f)))

# in f() exists propety 'param1'

```




