import sys

mesta = {}

class Mesta():

    def __init__(self):
        self.mesta = {}
        try:
            with open('cities.txt') as soubor:
                for radek in soubor:
                    kod, mesto = radek.rstrip().split(',', 1)
                    if kod in mesta:
                        self.mesta[kod].append(U(mesto))
                    else:
                        self.mesta[kod] = [mesto]
        except IOError as chyba:
            print("chyba", chyba)

    def Mesta(self):
        return self.mesta

c = Mesta()


for kod in sorted(c.Mesta().keys()):
    c.Mesta()[kod].sort()
    print(kod, ":",  ', '.join(c.Mesta()[kod]))

def dekorator_pozdravu(fuknkce_pozdravu):
    def obal(jmeno):
        return (fuknkce_pozdravu(jmeno)).capitalize()
    return obal

@dekorator_pozdravu
def pozdrav_me(jmeno):
    return "Ahoj " + jmeno


print(pozdrav_me(c.Mesta()['CZ'][0]))
