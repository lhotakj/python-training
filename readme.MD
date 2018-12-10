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

