# Gornati
#calcolatrice client per calcoServer.py versione multithread
import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 65432
NUM_WORKERS=2
def scegli_operazione_random():
    operazioni=["+","-","*","/"]
    indice=random.randrange(0,len(operazioni))
    return operazioni[indice]
def genera_richieste(num,address,port):
    start_time_thread= time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except Exception as e:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        print(e)
        sys.exit()
    #1. rimpiazzare questa parte con la generazione di operazioni e numeri random, non vogliamo inviare sempre 3+5 
    # primoNumero=3
    # operazione="+"
    # secondoNumero=5
    
    primoNumero=random.randint(0,1000)
    operazione=scegli_operazione_random()
    secondoNumero=random.randint(0,1000)
    
    #2. comporre il messaggio, inviarlo come json e ricevere il risultato
    messaggio=json.dumps({'primoNumero':primoNumero,'operazione':operazione,'secondoNumero':secondoNumero})
    print(f"Invio richiesta {messaggio}")
    s.sendall(messaggio.encode())
    data=s.recv(1024)

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        print(f"{threading.current_thread().name}: Risultato: {data.decode()}") # trasforma il vettore di byte in stringa
    s.close()
    end_time_thread=time.time()
    print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)

if __name__ == '__main__':
    start_time=time.time()
    # 3 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    [genera_richieste(num,SERVER_ADDRESS,SERVER_PORT) for num in range(1,NUM_WORKERS+1)]
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # 4 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # ad ogni iterazione appendo il thread creato alla lista threads
    threads=[threading.Thread(target=genera_richieste,args=(num,SERVER_ADDRESS,SERVER_PORT,)) for num in range(1,NUM_WORKERS+1)]
    # 5 avvio tutti i thread
    [thread.start() for thread in threads]
    # 6 aspetto la fine di tutti i thread 
    [thread.join() for thread in threads]
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    processes=[]
    # 7 ciclo per chiamare NUM_WORKERS volte la funzione genera richieste tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # ad ogni iterazione appendo il thread creato alla lista threads
    processes=[multiprocessing.Process(target=genera_richieste,args=(num,SERVER_ADDRESS,SERVER_PORT,)) for num in range(1,NUM_WORKERS+1)]
    # 8 avvio tutti i processi
    [process.start() for process in processes]
    # 9 aspetto la fine di tutti i processi 
    [process.join() for process in processes]
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)
