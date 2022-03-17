#nome del file : pagellaClientMulti.py
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json
import pprint

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=4
materie=["Italiano","Storia e Geografia","inglese","Matematica"]
studenti=["Gornati","Studente 1","Studente 2","Studente 3","Studente 4"]


def genera_studente():
  indice=random.randrange(0,len(studenti))
  return studenti[indice]
  
def genera_materia():
  indice=random.randrange(0,len(materie))
  return materie[indice]

#Versione 1 
def genera_richieste1(num,address,port):
  try:
    s=socket.socket()
    s.connect((address,port))
    print(f"{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
  except:
    print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
    sys.exit()
  #1. Generazione casuale:
  #   di uno studente (valori ammessi: 5 cognomi a caso tra cui il tuo cognome)
  studente=genera_studente()
  #   di una materia (valori ammessi: Matematica, Italiano, inglese, Storia e Geografia)
  materia=genera_materia()
  #   di un voto (valori ammessi 1 ..10)
  voto=random.randint(1,10)
  #   delle assenze (valori ammessi 1..5) 
  assenze=random.randint(1,5)
  #2. comporre il messaggio, inviarlo come json
  messaggio={'studente':studente,'materia':materia,'voto':voto,'assenze':assenze}
  #   esempio: {'studente': 'Studente4', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
  messaggio=json.dumps(messaggio)
  print(f"Invio dati {messaggio}")
  s.sendall(messaggio.encode("UTF-8"))
  #3. ricevere il risultato come json: {'studente':'Studente4','materia':'italiano','valutazione':'Gravemente insufficiente'}
  data=s.recv(1024)
  data=json.loads(data)
  if not data:
    print(f"{threading.current_thread().name}: Server non risponde. Exit")
  else:
    #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
    print(f"{threading.current_thread().name} {num+1}) La valutazione di {data['studente']} in {data['materia']} è {data['valutazione']}\n")
  s.close()

#Versione 2 
def genera_richieste2(num,address,port):
  try:
    s=socket.socket()
    s.connect((address,port))
    print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
  except:
    print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
    sys.exit()
  studente=genera_studente()
  pagella=[]
  for materia in materie:
    voto=random.randint(1,10)
    assenze=random.randint(1,5)
    pagella.append((materia,voto,assenze))
  pagella={'studente':studente,'pagella':pagella}
  # 1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
    # esempio: pagella={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9.5,3), ("Storia",8,2), ("Geografia",8,1)]}
  #2. comporre il messaggio, inviarlo come json
  messaggio=json.dumps(pagella)
  s.sendall(messaggio.encode("UTF-8"))
  print(f"Invio dati {messaggio}")
  #3  ricevere il risultato come json {'studente': 'Cognome1', 'media': 8.0, 'assenze': 8}
  data=s.recv(1024)
  data=json.loads(data)
  print(f"Ricevo dati {data}")
  if not data:
    print(f"{threading.current_thread().name}: Server non risponde. Exit")
  else:
    print(f"{threading.current_thread().name} {num+1}) Lo studente {data['studente']} ha una media di: {data['media']:.2f} e un totale di assenze: {data['assenze']:.2f}\n")
  s.close()

#Versione 3
def genera_richieste3(num,address,port):
  try:
    s=socket.socket()
    s.connect((address,port))
    print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
  except:
    print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
    sys.exit()
  messaggio={}
  for studente in studenti:
    pagella=[]
    for materia in materie:
      voto=random.randint(1,10)
      assenze=random.randint(1,10)
      pagella.append((materia,voto,assenze))
    messaggio[studente]=pagella
    #   1. Per ognuno degli studenti ammessi: 5 cognomi a caso scelti da una lista
    #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
    #   generazione di un voto (valori ammessi 1 ..10)
    #   e delle assenze (valori ammessi 1..5) 
    #   esempio: tabellone={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9,3), ("Storia",8,2), ("Geografia",8,1)],
    #                       "Cognome2":[("Matematica",7,2), ("Italiano",5,3), ("Inglese",4,12), ("Storia",5,2), ("Geografia",4,1)],
    #                        .....}
    
  #2. comporre il messaggio, inviarlo come json
  print("Invio dati")
  pprint.pprint(messaggio)
  messaggio=json.dumps(messaggio)
  s.sendall(messaggio.encode("UTF-8"))
  #3  ricevere il risultato come json e stampare l'output come indicato in CONSOLE CLIENT V.3
  data=s.recv(1024)
  data=json.loads(data)
  print(f"Ricevo dati")
  pprint.pprint(data)
  if not data:
    print(f"{threading.current_thread().name}: Server non risponde. Exit")
  else:
    for valutazioni in data:
      studente=valutazioni['studente']
      media=valutazioni['media']
      assenze=valutazioni['assenze']
      print(f"{threading.current_thread().name} {num+1}) Lo studente {studente} ha una media di: {media:.2f} e un totale di assenze: {assenze:.2f}")
  s.close()
  #....


if __name__ == '__main__':
    start_time=time.time()
    # PUNTO A) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)
    # alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    for i in range(NUM_WORKERS):
      # genera_richieste1(i,SERVER_ADDRESS,SERVER_PORT)
      genera_richieste2(i,SERVER_ADDRESS,SERVER_PORT)
      # genera_richieste3(i,SERVER_ADDRESS,SERVER_PORT)
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # PUNTO B) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)  
    # tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i thread e attenderne la fine
    for i in range(NUM_WORKERS):
      # threads.append(threading.Thread(target=genera_richieste1,args=(i,SERVER_ADDRESS,SERVER_PORT)))
      threads.append(threading.Thread(target=genera_richieste2,args=(i,SERVER_ADDRESS,SERVER_PORT)))
      # threads.append(threading.Thread(target=genera_richieste3,args=(i,SERVER_ADDRESS,SERVER_PORT)))
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    processes=[]
    # PUNTO C) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3) 
    # tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i processi e attenderne la fine
    for i in range(NUM_WORKERS):
      # processes.append(multiprocessing.Process(target=genera_richieste1,args=(i,SERVER_ADDRESS,SERVER_PORT)))
      processes.append(multiprocessing.Process(target=genera_richieste2,args=(i,SERVER_ADDRESS,SERVER_PORT)))
      # processes.append(multiprocessing.Process(target=genera_richieste3,args=(i,SERVER_ADDRESS,SERVER_PORT)))
    [process.start() for process in processes]
    [process.join() for process in processes]
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)