# Module
import secrets
import string

# Definirea "alfabetului"
litere = string.ascii_letters
numere = string.digits
cs = string.punctuation

alfabet1 = litere + numere + cs
alfabet2 = litere + numere

# Stabilire lungime parola
prl_l = 10

# Generare parola de tip caracter
prl = ''
for i in range(prl_l):
  prl += ''.join(secrets.choice(alfabet2))

print('Parola generata: ',prl)

# Generare parola cu caractere speciale
while True:
  prl = ''
  for i in range(prl_l):
    prl += ''.join(secrets.choice(alfabet1))

  if (any(char in cs for char in prl) and 
      sum(char in numere for char in prl)>=2):
          break
print('Parola generata cu caractere speciale: ',prl)

input()
