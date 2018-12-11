#!/usr/bin/env python3.3
import sys
import os
mesta={}
os.system('clear')
try:
  with open(sys.argv[1]) as soubor:
    for radek in soubor:
      kod,mesto=radek.rstrip().split(',',1)
      if kod in mesta:
        mesta[kod].append(mesto)
      else:
        mesta[kod]=[mesto]
except IOError as chyba:
  print("Nastala chyba:",chyba)
for kod in sorted(mesta.keys()):
  mesta[kod].sort()
  print(kod,":",','.join(mesta[kod]))

