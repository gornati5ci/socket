import time
import logging
from threading import Thread

# Inizializzazione del logger. Usiamo questo modulo eseguire i log alla console in modo più semplice
format="%(asctime)s: %(message)s"
logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")

def test(i):
  logging.info(f"{i} thread: iniziato")
  time.sleep(3)
  logging.info(f"{i} thread: finito")
  
# In questo caso quando eseguiamo il programma notiamo che grazie al join i thread vengono eseguiti in sequenza.
# In pratica il .join blocca l'esecuzione del codice fino a quando il thread t non ha finito l'esecuzione
for i in range(5):
  t=Thread(target=test,args=(i,))
  t.start()
  t.join()