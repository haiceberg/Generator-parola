# Generator-parola


## Descrierea Programului
Acest program Python generează două tipuri de parole: una formată din litere și cifre și una care include și caractere speciale.

## Funcționalități:
- Generare parolă simplă - O parolă formată doar din litere (mici și mari) și cifre.

- Generare parolă complexă - O parolă care conține litere, cifre și caractere speciale, garantând cel puțin două cifre și cel puțin un caracter special.

## Dependențe

* Python 3.x

* Modul `secrets`  (inclus implicit în biblioteca standard Python 3.x)

* Modul `string` (inclus implicit în biblioteca standard Python 3.x)

## Rezultat:


Programul va genera o parolă de 10 caractere (lungimea este stabilită prin variabila prl_l).

### **Intrare:** 

Va afișa întâi o parolă simplă (litere și cifre), apoi va genera o parolă complexă ce conține litere, cifre și caractere speciale. Aceasta va include cel puțin două cifre și cel puțin un caracter special.

### __Ieșire:__ 

La final, scriptul va afișa ambele parole generate pe ecran.

## Explicații:
* `secrets.choice()` : Funcția aleasă din modulul secrets alege un caracter aleatoriu dintr-un șir de caractere.

* `string.ascii_letters` : Conține toate literele de la A la Z (majuscule și minuscule).

* `string.digits` : Conține cifrele de la 0 la 9.

* `string.punctuation` : Conține toate caracterele speciale (semnele de punctuație).

## Personalizare:
Se poate schimba lungimea parolelor modificând valoarea variabilei prl_l.

În caz de adăugiri sau eliminări de caractere din seturile de caractere posibile (de exemplu, să incluzi sau să excluzi anumite caractere speciale), poți modifica variabilele alfabet1 și alfabet2.

## Exemplu de output:

Parola generata:  d7fK1QzTr4

Parola generata cu caractere speciale:  k1G*9wLf#4

## Contribuții
### Dacă dorești să îmbunătățești acest program sau să adaugi funcționalități suplimentare, te rog să contribui printr-un pull request.
