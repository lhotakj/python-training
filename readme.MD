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

