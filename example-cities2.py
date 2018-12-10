import sys

mesta={}
try:
    with open('cities.txt') as soubor:
        for radek in soubor:
            kod,mesto = radek.rstrip().split(',', 1)
            if kod in mesta:
                mesta[kod].append(mesto)
            else:
                mesta[kod]=[mesto]
except IOError as chyba:
    print("chyba", chyba)

for kod in sorted(mesta.keys()):
    mesta[kod].sort()
    print(kod, ":",  ', '.join(mesta[kod]))
