# -*- coding: utf-8 -*-
"""Gornati 9.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pXQFV_oxQeiCn-J4PIFvp0G9jCX_xFEp

# Esercizi con le Collezioni

# 0) Registro voti [[Esercizio su HackerRank](https://www.hackerrank.com/challenges/finding-the-percentage/problem)]
Hai a disposizione una lista di *N* studenti. Ogni lista contiene il nome dello studente e il suo voto in Matematica, Fisica e Chimica. I voti possono essere numeri con la virgola. Un utente inserisci un intero *N* seguito da il nome e i voti di N studenti. Il programma deve salvare le liste in un dizionario. Alla fine l'utente inserirà il nome di uno studente, il programma dovrà dare in output la media dei voti di tale studente arrotandata a due cifre dopo la virgola.
<br><br>
**ESEMPIO DI INPUT**
<br>
3<br>
Krishna 67 68 69<br>
Arjun 70 98 63<br>
Malika 52 56 60<br>
Malika<br>
<br>
**ESEMPIO DI OUTPUT**
<br>
56.00
<br><br>
**SUGGERIMENTO**
Possiamo applicare una trasformazione a tutti gli elementi di una collezione utilizzando la funzione *map*, questa funzione ritorna un generatore, di cui parleremo più avanti, che possiamo riconvertire in una collezione.
"""

n=int(input("Inserisci il numero degli studenti "))
materie=["Matematica","Fisica","Chimica"]
lista={}

for i in range(n):
  nome=input(f"Inserisci il nome dello studente {str(i+1)} ")
  voti=[]
  for materia in materie:
    voti.append(int(input(f"Inserisci il voto di {materia} di {nome} ")))
  lista[nome]=voti

nome=input("Inserisci il nome dello studente per la media voti ")
try:
  voti=lista[nome]
  somma=0
  for voto in voti:
    somma+=voto
  somma/=len(materie)
  print(f"La media dei voti dello studente {nome} è {(somma):.2f}")
except:
  print("Studente inesistente")

"""## 1. Pagelle scolastiche
Creiamo una struttura dati in grado di contenere i record di diversi studenti. La struttura sarà composta da un dizionario, con come chiave il nome dello studente e come valore una lista. La lista deve contenere delle tuple e ogni tupla deve avere alla prima posizione in nome della materia, alla seconda il voto e alla terza le ore di assenza. 
<table>
    <tr><td>Studente</td><td>Matematica</td><td>Italiano</td><td>Inglese</td><td>Storia</td><td>Geografia</td></tr>
    <tr><td>Giuseppe Gullo</td><td>VOTO: 9, ASSENZE: 0</td><td>VOTO: 7, ASSENZE: 3</td><td>VOTO: 7.5, ASSENZE: 4</td><td>VOTO: 7.5, ASSENZE: 4</td><td>VOTO: 5, ASSENZE: 7</td></tr>
    <tr><td>Antonio Barbera</td><td>VOTO: 8, ASSENZE: 1</td><td>VOTO: 6, ASSENZE: 1</td><td>VOTO: 9.5, ASSENZE: 0</td><td>VOTO: 8, ASSENZE: 2</td><td>VOTO: 8, ASSENZE: 1</td></tr>
    <tr><td>Nicola Spina</td><td>VOTO: 7.5, ASSENZE: 2</td><td>VOTO: 6, ASSENZE: 2</td><td>VOTO: 4, ASSENZE: 3</td><td>VOTO: 8.5, ASSENZE: 2</td><td>VOTO: 8, ASSENZE: 2</td></tr></table>

1. Popola la struttura dati con i dati qui sopra.
2. Aggiungi alla struttura dati la pagella di un nuovo studente chiamato Albert Einstein, con 10 in tutte le materie e nessu na ora di assenza.
3. Aggiungi Fisica a tutte le pagelle con le seguenti votazioni/assenze: Giuseppe Gullo 9.5/0, Antonino Barbera 8/1, Nicola Spina 8/3, Albert Einstein 10/0.
4. Stampa la tupla con le informazioni sulla materia Matematica per Giuseppe Gullo
5. Stampa la tupla con le informazioni sulla materia Inglese per Nicola Spina
6. Stampa solo il voto di Antonio Barbera in Geografia.
7. Stampa la media di tutte le materie di Nicola Spina.
8. Stampa la media di tutti i voti senza distinguere gli studenti.
9. Stampa la materia in cui ha fatto più assenze lo studente Nicola Spina.


"""

#1 Popolazione
elenco={'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
        'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
        'Nicola Spina':[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]}
#2 Aggiunta studente
elenco['Albert Einstein']=[("Matematica",10,0),("Italiano",10,0),("Inglese",10,0),("Storia",10,0),("Geografia",10,0)]
#3 Aggiunta fisica
elenco['Giuseppe Gullo'].append(("Fisica",9.5,0))
elenco['Antonio Barbera'].append(("Fisica",8,1))
elenco['Nicola Spina'].append(("Fisica",8,3))
elenco['Albert Einstein'].append(("Fisica",10,0))
#4 Matematica Gullo
print("Giuseppe Gullo, Matematica. Voto: "+str(elenco['Giuseppe Gullo'][0][1])+", assenze: "+str(elenco['Giuseppe Gullo'][0][2]))
#5 Inglese Spina
print("Nicola Spina, Inglese. Voto: "+str(elenco['Nicola Spina'][2][1])+", assenze: "+str(elenco['Nicola Spina'][2][2]))
#6 Geografia Barbera
print("Antonio Barbera, Inglese. Voto: "+str(elenco['Antonio Barbera'][2][1]))
#7 Media materie Spina
stud=elenco['Nicola Spina']
tot=0
for mat in stud:
  tot+=mat[1]
print("Media Nicola Spina: "+str(tot/6))
#8 Media tutti i voti
tot=0
for stud in elenco.values():
  for mat in stud:
    tot+=mat[1]
tot/=6*len(elenco)
print("Media totale: "+str(tot))
#9 Materia più assenze Spina
mate=""
ore=0
stud=elenco['Nicola Spina']
for mat in stud:
  if(mat[2]>ore):
    ore=mat[2]
    mate=mat[0]
print("Materia più ore assenza Nicola Spina: "+mate)

"""## 2. Gioco del tris ([risorsa](https://www.elexpo.net/archivio/sistemi/libro_automate_python/05.pdf))
Completare il codice seguente aggiungendo i seguenti controlli:

1.   Posizione libera/occupata
2.   Vittoria


"""

mosse=["top-L","top-M","top-R","mid-L","mid-M","mid-R","low-L","low-M","low-R"]
# function printBoard(board) {
def printBoard(board):
  print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
  print('-+-+-')
  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
  print('-+-+-')
  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def vittoria(board,turn):
  if board['top-L']==board['top-M'] and board['top-M']==board['top-R'] and board['top-L']!=" ":
    return turn
  if board['mid-L']==board['mid-M'] and board['mid-M']==board['mid-R'] and board['mid-L']!=" ":
    return turn
  if board['low-L']==board['low-M'] and board['low-M']==board['low-R'] and board['low-L']!=" ":
    return turn
  if board['top-L']==board['mid-L'] and board['mid-L']==board['low-L'] and board['top-L']!=" ":
    return turn
  if board['top-M']==board['mid-M'] and board['mid-M']==board['low-M'] and board['top-M']!=" ":
    return turn
  if board['top-R']==board['mid-R'] and board['mid-R']==board['low-R'] and board['top-R']!=" ":
    return turn
  if board['top-L']==board['mid-M'] and board['mid-M']==board['low-R'] and board['top-L']!=" ":
    return turn
  if board['top-R']==board['mid-M'] and board['mid-M']==board['low-L'] and board['top-R']!=" ":
    return turn
  vuote=0
  for cella in board.values():
    vuote+=1 if cella==" " else 0
  return vuote

def getNewBoard():
   return {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
theBoard=getNewBoard()
turn = 'X'
while True:
  printBoard(theBoard)
  while True:
    print('Turno di ' + turn + '. Quale posizione scegli?')
    move = input()
    if not move in mosse:
      print("Mossa non valida")
      print(mosse)
    elif theBoard[move]!=" ":
      print("Cella già occupata")
    else:
      break
  theBoard[move] = turn
  ris=vittoria(theBoard,turn)
  if ris=="X" or ris=="O":
    print("Ha vinto "+ris)
    printBoard(theBoard)
    print("--------")
    theBoard=getNewBoard()
  elif ris==0:
    print("Parità")
    theBoard=getNewBoard()
  turn="O" if turn=="X" else "X"
printBoard(theBoard)

"""# La mia rubrica 1

  Scrivi un programma per la gestione di una rubrica telefonica.
```
  Definisci un dizionario che rappresenti una rubrica di contatti, l'unico vincolo è di inserire almeno il nome e il numero di telefono.
  Definisci un altro oggetto che rappresenti la lista dei contatti (array di oggetti contatto).
  Implementa i metodi dell'oggetto per le seguenti operazioni:
      - Inserimento di un nuovo contatto
      - Visualizzazione dell'intera lista contatti
      - Modifica di uno contatto passando in input l'indice della posizione nell'array
      - Cancellazione di un contatto passando in input l'indice della posizione nell'array
      - Ricerca passando il nome e restituendo tutti i dati del singolo contatto.
```

Creare una struttura dati in grado di contenere i record di diversi contatti. La rubrica sarà composta da un dizionario, come chiave il cognome e il nome e come valore una lista [telefono, indirizzo, email]. 
<table>
    <tr><td>Contatto</td><td>Dati</td> </tr>
    <tr><td>Giuseppe Gullo</td><td>3393527822, Indirizzo 1, ggullo@mail.it</td></tr>
    <tr><td>Antonio Barbera</td><td>3393228442, Indirizzo 2, abarbera@mail.it</td> </tr>
    <tr><td>Nicola Spina</td><td>3383522812, Indirizzo 3, nspina@mail.it</td></tr></table>

Implementa un menu per eseguire i seguenti compiti:
1. Popola la rubrica
2. Aggiungi alla rubrica un nuovo contatto
3. Elimina dalla rubrica un contatto
4. Mostra i dati di un contatto
5. Mostra i dati di tutti i contatti
6. Modifica i dati di un contatto

Vincoli:
1. Tutti i campi devono essere compilati
2. Il telefono deve essere di 9 cifre
3. Il campo email deve contenere il simbolo @
4. Un contatto può essere aggiunto solo se non è già presente
5. Un contatto può essere eliminato o modificato solo se è già presente
6. Non è possibile modificare Nome e Cognome
7. Si devono utilizzare procedure aggiuntive per la lettura dei dati di contatto 

[Metodi dizionari](https://www.programmareinpython.it/video-corso-python-base/17-i-dizionari/)

``` 
0) Esci
1) Popola
2) Aggiungi
3) Elimina
4) Cerca
5) Mostra tutti
6) Modifica
Scegli :1

Quanti contatti vuoi inserire?1
Inserimento 1 contatto:

Nome = nome1 
Cognome = cognome1
Telefono (9 cifre) = 1234567
Telefono (9 cifre) = 123456789
Indirizzo  = indirizzo1
Email (@ richiesta) = miamailumanet.it
Email (@ richiesta) = miamail@umanet.it
{'COGNOME1 NOME1': ['123456789', 'indirizzo1', 'miamail@umanet.it']}

0) Esci
1) Popola
2) Aggiungi
3) Elimina
4) Cerca
5) Mostra tutti
6) Modifica
Scegli :2

Aggiunta di un contatto:

Nome = nome2
Cognome = cognome2
Telefono (9 cifre) = 987654321
Indirizzo  = indirizzo2
Email (@ richiesta) = miamail2@umanet.it
{   'COGNOME1 NOME1': ['123456789', 'indirizzo1', 'miamail@umanet.it'],
    'COGNOME2 NOME2': ['987654321', 'indirizzo2', 'miamail2@umanet.it']}

0) Esci
1) Popola
2) Aggiungi
3) Elimina
4) Cerca
5) Mostra tutti
6) Modifica
Scegli :3

Cancellazione di un contatto:

Nome = nome1
Cognome = cognome1
Contatto cancellato!
{'COGNOME2 NOME2': ['987654321', 'indirizzo2', 'miamail2@umanet.it']}

0) Esci
1) Popola
2) Aggiungi
3) Elimina
4) Cerca
5) Mostra tutti
6) Modifica
Scegli :4

Mostra dati di un contatto:

Nome = nome2
Cognome = cognome2
Dati contatto:
['987654321', 'indirizzo2', 'miamail2@umanet.it']

0) Esci
1) Popola
2) Aggiungi
3) Elimina
4) Cerca
5) Mostra tutti
6) Modifica
Scegli :6

Modifica dati di un contatto:

Nome = nome2
Cognome = cognome2
Dati del contatto:COGNOME2 NOME2
['987654321', 'indirizzo2', 'miamail2@umanet.it']
Aggiorna i dati (lascia in bianco i campi che non vuoi modificare):
Telefono (9 cifre) = 
Indirizzo  = 
Email (@ richiesta) = nuovaemail@umanet.it

0) Esci
1) Popola
2) Aggiungi
3) Elimina
4) Cerca
5) Mostra tutti
6) Modifica
Scegli :5

TUTTI I CONTATTI:
{'COGNOME2 NOME2': ['987654321', 'indirizzo2', 'nuovaemail@umanet.it']}
```
"""

import pprint
import re
pp=pprint.PrettyPrinter(indent=4)
contacts={}
nome=cognome=telefono=indirizzo=email=""
def leggiValori():
  global telefono,indirizzo,email
  regexEmail=re.compile(".*@.*\..*")
  regexTelefono=re.compile("\d{9,10}")
  telefono=input("Inserisci il telefono ")
  if len(telefono)!=0:
    while not regexTelefono.match(telefono):
      telefono=input("Inserisci il telefono ")
      if len(telefono)==0:
        break
  indirizzo=input("Inserisci indirizzo ")
  email=input("Inserisci email (@ richiesta) ")
  if len(email)!=0:
    while not regexEmail.match(email):
      email=input("Inserisci email (@ richiesta). Vuoto per annullare ")
      if len(email)==0:
        break
def leggiDati():
  global nome,cognome,telefono,indirizzo,email
  regexEmail=re.compile(".*@.*\..*")
  regexTelefono=re.compile("\d{9,10}")
  nome=input("Inserisci il nome ")
  while len(nome)==0:
    nome=input("Inserisci il nome ")
  cognome=input("Inserisci il cognome ")
  while len(cognome)==0:
    cognome=input("Inserisci il cognome ")
  telefono=input("Inserisci il telefono ")
  while not regexTelefono.match(telefono):
    telefono=input("Inserisci il telefono ")
  indirizzo=input("Inserisci indirizzo ")
  while len(indirizzo)==0:
    indirizzo=input("Inserisci indirizzo ")
  email=input("Inserisci email (@ richiesta) ")
  while not regexEmail.match(email):
    email=input("Inserisci email (@ richiesta) ")
  
def leggiChiave():
  global nome,cognome
  nome=input("Inserisci il nome =")
  while len(nome)==0:
    nome=input("Inserisci il nome =")
  cognome=input("Inserisci il cognome =")
  while len(cognome)==0:
    cognome=input("Inserisci il cognome =")

def popola(contatti=1):
   for cont in range (1,contatti+1):
     print(f"Inserimento {cont} contatto:")
     leggiDati()
     chiave=cognome+" "+nome
     valore=[telefono,indirizzo,email]
     contacts[chiave]=valore
     pp.pprint(contacts)

def elimina():
  leggiChiave()
  try:
    del contacts[cognome+" "+nome]
  except KeyError as ex:
    print("Contatto inesistente")
def cerca():
  leggiChiave()
  try:
    print(contacts[cognome+" "+nome])
  except KeyError as ex:
    print("Contatto inesistente")
def tutti():
  pp.pprint(contacts)
def modifica():
  leggiChiave()
  try:
    contatto=contacts[cognome+" "+nome]
    leggiValori()
    if telefono!="":
      contatto[0]=telefono
    if indirizzo!="":
      contatto[1]=indirizzo
    if email!="":
      contatto[2]=email
    print("Modifica effettuata con successo")
  except KeyError as ex:
    print("Contatto inesistente")


scelta=1
while (scelta!=0):
  print('0) Esci')
  print('1) Popola')
  print('2) Aggiungi')
  print('3) Elimina')
  print('4) Cerca')
  print('5) Mostra tutti')
  print('6) Modifica')
  scelta=int(input('Scegli :'))
  if scelta==1:
    i=int(input("Quanti contatti vuoi inserire?"))
    popola(i)
  elif scelta==2:
    popola()
  elif scelta==3:
    elimina()
  elif scelta==4:
    cerca()
  elif scelta==5:
    tutti()
  elif scelta==6:
    modifica()