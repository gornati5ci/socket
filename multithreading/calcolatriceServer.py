# server.py
import socket
import json
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT=65432
# Creo una funzione con lo scopo di interagire con il client
def ricevi_comandi(sock_service,addr_client):
  print("Avviato")
  while True:
    data=sock_service.recv(1024)
    if not data:
      break
    data=data.decode()
    data=json.loads(data)
    primoNumero=data['primoNumero']
    operazione=data['operazione']
    secondoNumero=data['secondoNumero']
    ris=""
    if operazione=="+":
      ris=primoNumero+secondoNumero
    elif operazione=="-":
      ris=primoNumero-secondoNumero
    elif operazione=="*":
      ris=primoNumero*secondoNumero
    elif operazione=="/":
      if secondoNumero==0:
        ris="Non puoi dividere per 0"
      else:
        ris=primoNumero/secondoNumero
    elif operazione=="%":
      ris=primoNumero%secondoNumero
    else:
      ris="Operazione non riconosciuta"
    ris=str(ris)
    sock_service.sendall(ris.encode("UTF-8"))
  sock_service.close()
# Questa funzione genera un Thread ogni volta che un client si collega
def ricevi_connessioni(sock_listen):
  while True:
    sock_service,addr_client=sock_listen.accept()
    print("\nConnessione ricevuta da "+str(addr_client))
    print("\nCreo un thread per servire le richieste")
    try:
      Thread(target=ricevi_comandi,args=(sock_service,addr_client)).start()
    except:
      print("Il thread non si avvia")
      sock_listen.close()
# Questa è la funzione che viene chiamata quando sia avvia il server.
# Esegue configurazioni per l'avvio del server
def avvia_server(indirizzo,porta):
  sock_listen=socket.socket()
  sock_listen.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
  sock_listen.bind((indirizzo,porta))
  sock_listen.listen(5)
  print("Server in ascolto su %s." % str((indirizzo,porta)))
  ricevi_connessioni(sock_listen)
  
if __name__=="__main__":
  avvia_server(SERVER_ADDRESS,SERVER_PORT)

