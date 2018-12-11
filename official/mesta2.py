#!/usr/bin/env python3.3
import re
import sys
mesta={}
try:
  with open(sys.argv[1]) as soubor:
    for radek in soubor:
      m=re.search('^([A-Z]{2,3}),([a-z]+( [a-z]+)*)$',radek,re.I)
      if m:
        kod,mesto=m.group(1),m.group(2)
        if kod in mesta:
          mesta[kod].append(mesto)
        else:
          mesta[kod]=[mesto]
except IOError as chyba:
  print("Nastala chyba:",chyba)
for kod in sorted(mesta.keys()):
  mesta[kod].sort()
  print(kod,":",','.join(mesta[kod]))

