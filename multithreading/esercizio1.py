from threading import Thread
import time, datetime

#Creo una funzione che verrà eseguita in un thread diverso dal main
def thread1():
  print("Thread 1 iniziato") # Stampo nella console quando inizia il thread 1
  time.sleep(10) # Metto il thread in pausa per 10 secondi
  print("Thread 1 finito") # Stampo nella console quando finisce il thread 1
  
#Creo una seconda funzione da eseguire in un altro thread
def thread2():
  print("Thread 2 iniziato")
  time.sleep(4) # Questa volta metto il thread in pausa per 4 secondi
  print("Thread 2 finito")
  
# Faccio iniziare il main
print("Main iniziato")
start_time=time.time() # Prendo il tempo di inizio del main
# Creo i due thread
t1=Thread(target=thread1)
t2=Thread(target=thread2)
# Faccio partire i due thread
t1.start()
t2.start()
# Metto il main in pausa due secondi
time.sleep(2)
# Prendo il tempo di inizio del main
end_time=time.time()
# Stampo quanto ci ha messo il main ad essere eseguito(in secondi)
print(f"Main finito in {end_time-start_time}")

# L'output mostra come i thread siano stati eseguiti "contemporaneamente", impiegando un tempo totale di 10 secondi(circa)